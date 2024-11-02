from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, RecipeStatistics, RecipeCollection
from django.http import HttpResponseNotFound, HttpResponseForbidden
from django.db.models import Avg, Count, Q
from .forms import RecipeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
# Create your views here.
def all_recipes(request):
    title = request.GET.get('title')

    if title and len(title) > 3:
        found_recipes = Recipe.objects.filter(recipe_name__contains=title)
    else:
        found_recipes = Recipe.objects.all()

    found_recipes_aggregation = found_recipes.aggregate(
        Avg('statistics__recipe_rate'),
        Count('id'),
        favourite_recipes = Count('id', filter=Q(statistics__recipe_rate__gt=8.0))
    )
    type_counts = Recipe.objects.values('type_of_meal').annotate(meal_count=Count('id')).order_by('-type_of_meal')
    category_counts = Recipe.objects.values('category').annotate(category_count=Count('id'))

    context = {
        'recipes': found_recipes,
        'aggregate_data': found_recipes_aggregation,
        'meal_type': type_counts,
        'category_counts': category_counts,
        'filter_title': title
    }

    return render(request, 'recipe/all_recipes.html', context)

@login_required
def recipe_details(request,id):
    found_recipe = Recipe.objects.get(pk=id)
    if not found_recipe:
        return HttpResponseNotFound('Nie znaleziono takiego przepisu')
    context = {
        'recipe': found_recipe
    }
    return render(request, 'recipe/recipe_details.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe_data = form.cleaned_data
            stats = RecipeStatistics.objects.create(recipe_rate=0, number_of_ratings=0)

            Recipe.objects.create(
                recipe_id=recipe_data['recipe_id'],
                recipe_name=recipe_data['recipe_name'],
                type_of_meal=recipe_data['type_of_meal'],
                ingredients=recipe_data['ingredients'],
                preparation=recipe_data['preparation'],
                difficulty_level=recipe_data['difficulty_level'],
                preparation_time=recipe_data['preparation_time'],
                quantity_of_servings=recipe_data['quantity_of_servings'],
                energy_value_kcal=recipe_data['energy_value_kcal'],
                protein_g=recipe_data['protein_g'],
                fat_g=recipe_data['fat_g'],
                carbohydrates_g=recipe_data['carbohydrates_g'],
                lactose_free=recipe_data['lactose_free'],
                gluten_free=recipe_data['gluten_free'],
                dairy_free=recipe_data['dairy_free'],
                vegetarian_or_vegan=recipe_data['vegetarian_or_vegan'],
                meat=recipe_data['meat'],
                fish=recipe_data['fish'],
                category=recipe_data['category'],
                images=recipe_data['images'],
                statistics=stats,
            )

            return redirect('all_recipes_url')

    form = RecipeForm()
    context = {
        'recipe_form': form
    }

    return render(request, 'recipe/add_recipe.html', context)

@login_required
def all_collections(request):
    logged_user = request.user

    if request.method == 'POST':
        name = request.POST['collection_name']
        RecipeCollection.objects.create(name=name,owner=logged_user)
        return redirect('all_collections_url')

    recipe_collections = RecipeCollection.objects.filter(owner=logged_user).annotate(recipe_count=Count('id'))

    context = {
        'collections': recipe_collections
    }
    return render(request, 'recipe/all_collections.html', context)

@login_required
def collection_details(request, id):
    login_user = request.user
    collection = RecipeCollection.objects.get(pk=id)

    if collection.owner.id != login_user.id:
        return HttpResponseForbidden('Nie masz dostępu do tej kolekcji')

    recipes = collection.recipes.all()

    recipe_name = request.GET.get('recipe_name')
    difficulty_level = request.GET.get('difficulty_level')
    type_of_meal = request.GET.get('type_of_meal')

    if recipe_name:
        recipes = recipes.filter(recipe_name__icontains=recipe_name)
    if difficulty_level:
        recipes = recipes.filter(difficulty_level=difficulty_level)
    if type_of_meal:
        recipes = recipes.filter(type_of_meal=type_of_meal)

    available_recipes = Recipe.objects.exclude(id__in=collection.recipes.all())

    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            collection.recipes.add(recipe)
            return redirect('collection_details_url', id=collection.id)
        except Recipe.DoesNotExist:
            pass

    return render(request, 'recipe/collection_details.html', {
        'collection': collection,
        'recipes': recipes,
        'available_recipes': available_recipes
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    statistics = get_object_or_404(RecipeStatistics, recipe=recipe)

    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe.recipe_id = form.cleaned_data['recipe_id']
            recipe.recipe_name = form.cleaned_data['recipe_name']
            recipe.type_of_meal = form.cleaned_data['type_of_meal']
            recipe.ingredients = form.cleaned_data['ingredients']
            recipe.preparation = form.cleaned_data['preparation']
            recipe.difficulty_level = form.cleaned_data['difficulty_level']
            recipe.preparation_time = form.cleaned_data['preparation_time']
            recipe.quantity_of_servings = form.cleaned_data['quantity_of_servings']
            recipe.energy_value_kcal = form.cleaned_data['energy_value_kcal']
            recipe.protein_g = form.cleaned_data['protein_g']
            recipe.fat_g = form.cleaned_data['fat_g']
            recipe.carbohydrates_g = form.cleaned_data['carbohydrates_g']
            recipe.lactose_free = form.cleaned_data['lactose_free']
            recipe.gluten_free = form.cleaned_data['gluten_free']
            recipe.dairy_free = form.cleaned_data['dairy_free']
            recipe.vegetarian_or_vegan = form.cleaned_data['vegetarian_or_vegan']
            recipe.meat = form.cleaned_data['meat']
            recipe.fish = form.cleaned_data['fish']
            recipe.category = form.cleaned_data['category']
            recipe.images = form.cleaned_data['images']
            recipe.save()

            statistics.recipe_rate = form.cleaned_data['recipe_rate']
            statistics.save()
            return redirect('all_recipes_url')
    else:
        initial_data = {
            'recipe_id': recipe.recipe_id,
            'recipe_name': recipe.recipe_name,
            'type_of_meal': recipe.type_of_meal,
            'ingredients': recipe.ingredients,
            'preparation': recipe.preparation,
            'difficulty_level': recipe.difficulty_level,
            'preparation_time': recipe.preparation_time,
            'quantity_of_servings': recipe.quantity_of_servings,
            'energy_value_kcal': recipe.energy_value_kcal,
            'protein_g': recipe.protein_g,
            'fat_g': recipe.fat_g,
            'carbohydrates_g': recipe.carbohydrates_g,
            'lactose_free': recipe.lactose_free,
            'gluten_free': recipe.gluten_free,
            'dairy_free': recipe.dairy_free,
            'vegetarian_or_vegan': recipe.vegetarian_or_vegan,
            'meat': recipe.meat,
            'fish': recipe.fish,
            'category': recipe.category,
            'images': recipe.images,
            'recipe_rate': statistics.recipe_rate
        }
        form = RecipeForm(initial=initial_data)

    context = {
        'recipe_form': form,
        'recipe': recipe,
    }
    return render(request, 'recipe/edit_recipe.html', context)
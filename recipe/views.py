from django.shortcuts import render
from .models import Recipe
from django.http import HttpResponseNotFound


# Create your views here.
def all_recipes(request):
    found_recipes = Recipe.find_all_recipes()
    context = {
        'recipes': found_recipes
    }
    return render(request, 'recipe/all_recipes.html', context)

def recipe_details(request, recipe_id):
    found_recipe = Recipe.find_all_recipes()
    for r in found_recipe:
        if r.recipe_id == recipe_id:
            context = {
                'recipe': r
            }
            return render(request, 'recipe/recipe_details.html', context)
    return HttpResponseNotFound('Nie znaleziono takiego przepisu')
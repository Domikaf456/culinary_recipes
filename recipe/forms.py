from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator
from .choices import (TYPE_OF_MEAL_CHOICES, DIFFICULTY_CHOICES, CATEGORY_CHOICES, LACTOSE_CHOICES, GLUTEN_CHOICES,
                      DAIRY_CHOICES, VEGETARIAN_VEGAN_CHOICES, MEAT_CHOICES, FISH_CHOICES)
from .models import Recipe, RecipeStatistics


class RecipeForm(forms.Form):
    recipe_id = forms.CharField(label="Numer przepisu", max_length=255)
    recipe_name = forms.CharField(label="Nazwa przepisu", max_length=1000, validators=[MinLengthValidator(5), MaxLengthValidator(1000)])
    type_of_meal = forms.ChoiceField(label="Typ posiłku", choices=TYPE_OF_MEAL_CHOICES)
    ingredients = forms.CharField(label="Składniki", validators=[MinLengthValidator(10), MaxLengthValidator(3000)], widget=forms.Textarea(attrs={
        'rows': 10}))
    preparation = forms.CharField(label="Przygotowanie", validators=[MinLengthValidator(10)],
                                  widget=forms.Textarea(attrs={'rows': 10}))
    difficulty_level = forms.ChoiceField (label="Poziom trudności", choices=DIFFICULTY_CHOICES)
    preparation_time = forms.IntegerField(label="Czas przygotowania", validators=[MinValueValidator(0)])
    quantity_of_servings = forms.IntegerField(label="Ilość porcji", validators=[MinValueValidator(0)])
    energy_value_kcal = forms.CharField(label="Ilość kalorii w porcji [kcal]", max_length=255, validators=[MinLengthValidator(0)])
    protein_g = forms.FloatField(label="Białko [g]", validators=[MinValueValidator(0)])
    fat_g = forms.FloatField(label="Tłuszcz [g]", validators=[MinValueValidator(0)])
    carbohydrates_g = forms.FloatField(label="Węglowodany [g]", validators=[MinValueValidator(0)])
    lactose_free = forms.ChoiceField(label="Bez laktozy", choices=LACTOSE_CHOICES, required=False)
    gluten_free = forms.ChoiceField(label="Bez glutenu", choices=GLUTEN_CHOICES, required=False)
    dairy_free = forms.ChoiceField(label="Bez mleka", choices=DAIRY_CHOICES, required=False)
    vegetarian_or_vegan = forms.ChoiceField(label="Wegetariańskie lub wegańskie?", choices=VEGETARIAN_VEGAN_CHOICES, required=False)
    meat = forms.ChoiceField(label="Danie mięsne", choices=MEAT_CHOICES, required=False)
    fish = forms.ChoiceField(label="Danie rybne", choices=FISH_CHOICES, required=False)
    category = forms.ChoiceField (label="Kategoria dania", choices=CATEGORY_CHOICES)
    images = forms.URLField(label="Zdjęcie", max_length=1000)
    recipe_rate = forms.DecimalField(label="Ocena", max_digits=10, decimal_places=2)


def __init__(self, *args, **kwargs):
    super(RecipeForm, self).__init__(*args, **kwargs)
    for visible_field in self.visible_fields():
        visible_field.field.widget.attrs['class'] = 'uk-input uk-margin-small-bottom'

class RecipeStatisticsForm(forms.ModelForm):
    class Meta:
        model = RecipeStatistics
        fields = ['recipe_rate']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'recipe_id', 'recipe_name', 'type_of_meal', 'ingredients', 'preparation',
            'difficulty_level', 'preparation_time', 'quantity_of_servings',
            'energy_value_kcal', 'protein_g', 'fat_g', 'carbohydrates_g',
            'lactose_free', 'gluten_free', 'dairy_free', 'vegetarian_or_vegan',
            'meat', 'fish', 'category', 'images'
        ]

def __init__(self, *args, **kwargs):
    super(RecipeForm, self).__init__(*args, **kwargs)
    self.fields['statistics__recipe_rate'].label = 'Recipe Rate'




import csv

from django.db import models
from .choices import TYPE_OF_MEAL_CHOICES, DIFFICULTY_CHOICES, CATEGORY_CHOICES
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, URLValidator
from django.contrib.auth.models import User

class RecipeStatistics(models.Model):
    recipe_rate = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(0), MaxValueValidator(10)])
    number_of_ratings = models.IntegerField(validators=[MinValueValidator(0)])

class Recipe(models.Model):
    recipe_id = models.CharField(max_length=255, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=3)
    recipe_name = models.CharField(max_length=1000, validators=[MinLengthValidator(5)])
    type_of_meal = models.CharField(max_length=255, choices=TYPE_OF_MEAL_CHOICES)
    ingredients = models.TextField(validators=[MinLengthValidator(10)])
    preparation = models.TextField(validators=[MinLengthValidator(10)])
    difficulty_level = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    preparation_time = models.IntegerField(validators=[MinValueValidator(0)])
    quantity_of_servings = models.IntegerField(validators=[MinValueValidator(0)])
    energy_value_kcal = models.CharField(max_length=255, validators=[MinLengthValidator(0)])
    protein_g = models.FloatField(validators=[MinValueValidator(0)])
    fat_g = models.FloatField(validators=[MinValueValidator(0)])
    carbohydrates_g = models.FloatField(validators=[MinValueValidator(0)])
    lactose_free = models.CharField(max_length=255, blank=True, null=True)
    gluten_free = models.CharField(max_length=255, blank=True, null=True)
    dairy_free = models.CharField(max_length=255, blank=True, null=True)
    vegetarian_or_vegan = models.CharField(max_length=255, blank=True, null=True)
    meat = models.CharField(max_length=255, blank=True, null=True)
    fish = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, blank=True, null=True)
    images = models.URLField(max_length=1000, blank=True, null=True)
    statistics = models.OneToOneField(RecipeStatistics, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.recipe_name}'


class RecipeCollection(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)


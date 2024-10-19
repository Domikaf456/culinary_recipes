import csv

from django.db import models

# Create your models here.
class Recipe:

    def __init__(self, recipe_id, recipe_name, type_of_meal, ingredients, preparation, energy_value_kcal, protein_g,
                 fat_g,	carbohydrates_g, difficulty_level,preparation_time, quantity_of_servings,
                 recipe_rate, number_of_ratings,lactose_free, gluten_free, dairy_free, vegetarian_or_vegan, meat, fish, category, images):
        self.recipe_id = recipe_id
        self.recipe_name = recipe_name
        self.type_of_meal = type_of_meal
        self.ingredients = ingredients
        self.preparation = preparation
        self.energy_value_kcal = energy_value_kcal
        self.protein_g = protein_g
        self.fat_g = fat_g
        self.carbohydrates_g = carbohydrates_g
        self.difficulty_level = difficulty_level
        self.preparation_time = preparation_time
        self.quantity_of_servings = quantity_of_servings
        self.recipe_rate = recipe_rate
        self.number_of_ratings = number_of_ratings
        self.lactose_free = lactose_free
        self.gluten_free = gluten_free
        self.dairy_free = dairy_free
        self.vegetarian_or_vegan = vegetarian_or_vegan
        self.meat = meat
        self.fish = fish
        self.category = category
        self.images = images

    @staticmethod
    def find_all_recipes():
        recipes_list = []
        with open('recipe/migrations/recipes_file_csv.csv', 'r', encoding='UTF-8') as file:
            reader = csv.DictReader(file, delimiter=',')

            for row in reader:
                recipes_list.append(Recipe(
                    row['recipe_id'],
                    row['recipe_name'],
                    row['type_of_meal'],
                    row['ingredients'],
                    row['preparation'],
                    row['energy_value_kcal'],
                    float(row['protein_g']),
                    float(row['fat_g']),
                    float(row['carbohydrates_g']),
                    row['difficulty_level'],
                    int(row['preparation_time']),
                    float(row['quantity_of_servings']),
                    float(row['recipe_rate']),
                    int(row['number_of_ratings']),
                    row['lactose_free'],
                    row['gluten_free'],
                    row['dairy_free'],
                    row['vegetarian_or_vegan'],
                    row['meat'],
                    row['fish'],
                    row['category'],
                    row['images']
                ))
        return recipes_list

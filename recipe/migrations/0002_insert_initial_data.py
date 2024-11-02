from django.db import migrations
from recipe.models import Recipe, RecipeStatistics
import csv
import datetime

def load_initial_data(apps, schema_editor):
    recipes_list = []
    with open('recipe/migrations/recipes_file_csv.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file, delimiter=',')

        for row in reader:
            statistics = RecipeStatistics(recipe_rate=float(row['recipe_rate']), number_of_ratings=int(row['number_of_ratings']))
            statistics.save()

            Recipe.objects.create(
                recipe_id=row['recipe_id'],
                type_of_meal=row['type_of_meal'],
                recipe_name=row['recipe_name'],
                ingredients=row['ingredients'],
                preparation=row['preparation'],
                difficulty_level=row['difficulty_level'],
                preparation_time=int(row['preparation_time']),
                quantity_of_servings=float(row['quantity_of_servings']),
                energy_value_kcal = row['energy_value_kcal'],
                protein_g = float(row['protein_g']),
                fat_g = float(row['fat_g']),
                carbohydrates_g = float(row['carbohydrates_g']),
                lactose_free=row['lactose_free'],
                gluten_free=row['gluten_free'],
                dairy_free=row['dairy_free'],
                vegetarian_or_vegan=row['vegetarian_or_vegan'],
                meat=row['meat'],
                fish=row['fish'],
                category=row['category'],
                images=row['images'],
                statistics=statistics
            )

class Migration(migrations.Migration):

    initial = False

    dependencies = [
        ('recipe','0001_initial')
    ]

    operations = [
        migrations.RunPython(load_initial_data)
    ]
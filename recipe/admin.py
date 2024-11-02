from django.contrib import admin
from recipe.models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_filter = ("type_of_meal", "difficulty_level", "category")
    list_display = ("recipe_name", "type_of_meal", "difficulty_level", "category")



# Register your models here.
admin.site.register(Recipe, RecipeAdmin)

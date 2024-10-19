from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_recipes, name='all_recipes_url'),
    path('<recipe_id>', views.recipe_details, name='recipe_details_url'),
]
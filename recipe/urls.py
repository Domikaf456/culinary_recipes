from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_recipes, name='all_recipes_url'),
    path('add', views.add_recipe, name='add_recipe_url'),
    path('collections', views.all_collections, name='all_collections_url'),
    path('<int:id>', views.recipe_details, name='recipe_details_url'),
    path('collections/<int:id>', views.collection_details, name='collection_details_url'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe_url')

]
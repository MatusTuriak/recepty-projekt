from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.recipe_list, name='recipes'),
    path('recipes/<int:id>/', views.recipe_detail, name='detail'),
    path('add/', views.add_recipe, name='add_recipe'),
        # CATEGORY CRUD
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_create, name='category_create'),
    path('categories/<int:pk>/edit/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # INGREDIENT CRUD
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('ingredients/add/', views.ingredient_create, name='ingredient_create'),
    path('ingredients/<int:pk>/edit/', views.ingredient_update, name='ingredient_update'),
    path('ingredients/<int:pk>/delete/', views.ingredient_delete, name='ingredient_delete'),

    path('recipes/<int:id>/edit/', views.update_recipe, name='update_recipe'),
    path('recipes/<int:id>/delete/', views.delete_recipe, name='delete_recipe'),
]
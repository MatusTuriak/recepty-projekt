from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.recipe_list, name='recipes'),
    path('recipes/<int:id>/', views.recipe_detail, name='detail'),
    path('add/', views.add_recipe, name='add_recipe'),
]
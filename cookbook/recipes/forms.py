from django import forms
from .models import Recipe
from .models import Category, Ingredient


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'description', 'allergen_type']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
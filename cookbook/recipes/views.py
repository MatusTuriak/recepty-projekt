from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeIngredient
from .forms import RecipeForm


def index(request):
    return render(request, 'recipes/index.html')


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes.html', {'recipes': recipes})


def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)

    return render(request, 'recipes/detail.html', {
        'recipe': recipe,
        'ingredients': ingredients
    })


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RecipeForm()

    return render(request, 'recipes/form.html', {'form': form})
from django.shortcuts import render,redirect, get_object_or_404
from .models import Recipe, RecipeIngredient, Category, Ingredient
from .forms import RecipeForm, CategoryForm, IngredientForm


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

# CATEGORY CRUD

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'recipes/category_list.html', {'categories': categories})


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'recipes/category_form.html', {'form': form})


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'recipes/category_form.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('category_list')

    return render(request, 'recipes/category_confirm_delete.html', {'category': category})


# INGREDIENT CRUD

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'recipes/ingredient_list.html', {'ingredients': ingredients})


def ingredient_create(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()

    return render(request, 'recipes/ingredient_form.html', {'form': form})


def ingredient_update(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)

    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm(instance=ingredient)

    return render(request, 'recipes/ingredient_form.html', {'form': form})


def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)

    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient_list')

    return render(request, 'recipes/ingredient_confirm_delete.html', {'ingredient': ingredient})

def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes')
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/form.html', {'form': form})


def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')

    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})
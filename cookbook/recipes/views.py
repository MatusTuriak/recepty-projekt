from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, RecipeIngredient, Category, Ingredient
from .forms import RecipeForm, CategoryForm, IngredientForm, RecipeIngredientForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'recipes/index.html')


def recipe_list(request):
    recipes = Recipe.objects.all()

    search = request.GET.get('search')
    category = request.GET.get('category')
    difficulty = request.GET.get('difficulty')
    ingredient = request.GET.get('ingredient')

    if search:
        recipes = recipes.filter(name__icontains=search)

    if category:
        recipes = recipes.filter(category_id=category)

    if difficulty:
        recipes = recipes.filter(difficulty=difficulty)

    if ingredient:
        recipes = recipes.filter(recipeingredient__ingredient_id=ingredient)

    categories = Category.objects.all()
    ingredients = Ingredient.objects.all()

    return render(request, 'recipes/recipes.html', {
        'recipes': recipes,
        'categories': categories,
        'ingredients': ingredients
    })


def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)

    return render(request, 'recipes/detail.html', {
        'recipe': recipe,
        'ingredients': ingredients
    })


@login_required
def add_recipe(request):
    ingredients = Ingredient.objects.all()

    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save()

            selected_ingredients = request.POST.getlist('ingredients')

            for ingredient_id in selected_ingredients:
                RecipeIngredient.objects.create(
                    recipe=recipe,
                    ingredient_id=ingredient_id,
                    quantity=0,
                    unit=''
                )

            return redirect('detail', id=recipe.id)
    else:
        form = RecipeForm()

    return render(request, 'recipes/form.html', {
        'form': form,
        'ingredients': ingredients
    })


@login_required
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


@login_required
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')

    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})


@login_required
def add_recipe_ingredient(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == 'POST':
        form = RecipeIngredientForm(request.POST)

        if form.is_valid():
            recipe_ingredient = form.save(commit=False)
            recipe_ingredient.recipe = recipe
            recipe_ingredient.save()
            return redirect('detail', id=recipe.id)
    else:
        form = RecipeIngredientForm()

    return render(request, 'recipes/recipe_ingredient_form.html', {
        'form': form,
        'recipe': recipe
    })


# CATEGORY CRUD

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'recipes/category_list.html', {'categories': categories})


@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'recipes/category_form.html', {'form': form})


@login_required
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


@login_required
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


@login_required
def ingredient_create(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()

    return render(request, 'recipes/ingredient_form.html', {'form': form})


@login_required
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


@login_required
def ingredient_delete(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)

    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient_list')

    return render(request, 'recipes/ingredient_confirm_delete.html', {'ingredient': ingredient})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes')
    else:
        form = UserCreationForm()

    return render(request, 'recipes/register.html', {'form': form})

@login_required
def toggle_favorite(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if recipe.favorites.filter(id=request.user.id).exists():
        recipe.favorites.remove(request.user)
    else:
        recipe.favorites.add(request.user)

    return redirect('detail', id=recipe.id)


@login_required
def favorite_recipes(request):
    recipes = Recipe.objects.filter(favorites=request.user)
    return render(request, 'recipes/favorites.html', {'recipes': recipes})
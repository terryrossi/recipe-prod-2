from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Recipe
from ingredients.models import Ingredient
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import pandas as pd
from .utils import get_username_from_id, get_chart

#to protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SearchForm

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes_home.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Recipe.objects.filter(name__icontains=query)
        else:
            return Recipe.objects.all()
         


class RecipeDetailView(LoginRequiredMixin, DetailView): #class-based “protected” view
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

@login_required
def records(request):
    # create an instance of SearchForm and pass it to the template
    form = SearchForm(request.POST or None)

    # initialize variables
    ingredient_name = None # create an empty string to store the ingredient name
    recipes_with_ingredient = [] # create an empty list to store recipes with the ingredient
    search_df = None # create an empty dataframe to store the search results
    chart = None # create an empty string to store the chart
    ingredient_not_found = '' # create an empty string to store the ingredient not found 💆‍♂️ 
    recipe_not_found = '' # create a boolean to store the recipe not found

    # if the form is submitted and valid, then we will process the data
    if request.method == 'POST' and form.is_valid():
      # read ingredient and chart_type from the form
        ingredient_name = request.POST.get('ingredient').strip()
        chart_type = request.POST.get('chart_type')
        print(ingredient_name)
        print(chart_type)

        # get the ingredient object from the database
        try:
            ingredient = Ingredient.objects.filter(name__icontains=ingredient_name)

           
                # get the recipes that contain the ingredient
            recipes_with_ingredient = Recipe.objects.filter(ingredients__in=ingredient).distinct()

                # print ('recipes_with_ingredient : ')
                # print (recipes_with_ingredient)
                # print ('recipes_with_ingredient.values() : ')
                # print (recipes_with_ingredient.values())
                # print ('recipes_with_ingredient.values_list() : ')
                # print (recipes_with_ingredient.values_list())
                # print ('total_recipes : ')
                # print (total_recipes)

            if recipes_with_ingredient.exists():
                # create a dataframe from the recipes
                search_df = pd.DataFrame(list(recipes_with_ingredient.values()))

                # total number of recipes in the db for the chart
                total_recipes = Recipe.objects.all().count()

                # Generate HTML links for each recipe name
                search_df['Link'] = search_df.apply(lambda row: f'<a href="{reverse("recipes:recipe_detail", kwargs={"pk": row["id"]})}">{row["name"]}</a>', axis=1)


                # add a new column to the dataframe to store the username of the author
                search_df['author'] = search_df['userid_id'].apply(get_username_from_id)

                # add a new column to the dataframe to store the total number of recipes
                search_df['total_recipes'] = total_recipes

                # create a chart from the dataframe
                chart = get_chart(chart_type, search_df, labels=search_df['name'])

                # convert the dataframe to HTML
                search_df = search_df.to_html(escape=False)

            else:
                recipe_not_found = "Recipe not Found"

        except Ingredient.DoesNotExist:
                ingredient_not_found = 'Ingredient not Found'


    # pack up data to be sent to template in the context dictionary
    context = {
        'form': form,
        'search_df': search_df,
        'chart': chart,
        'ingredient_not_found': ingredient_not_found,
        'recipe_not_found': recipe_not_found,
    }
    print('ingredient_not_found : ')
    print(ingredient_not_found)
    print('recipe_not_found : ')
    print(recipe_not_found)

    # Load the sales/records.html template with the context dictionary

    return render(request, 'recipes/records.html', context)

# Create a view for the about me page
def about_me(request):
    return render(request, 'recipes/about_me.html')
from django.urls import path
from .views import RecipeListView, RecipeDetailView
from .views import records, about_me

# we specify the app_name variable to avoid confusion with other apps
app_name = 'recipes'

urlpatterns = [
    # we specify here that we want to use the home function 
    # from the views.py file when the user goes to the root URL
    path('',  RecipeListView.as_view(), name='recipes_home'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    # path('', records, name='records'),
    path('search/', records, name='records'),
    path('about-me/', about_me, name='about_me'), 
]

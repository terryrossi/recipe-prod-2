from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Ingredient
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IngredientListView(LoginRequiredMixin, ListView):           #class-based view
   model = Ingredient                        #specify model
   template_name = 'recipes/ingredients_home.html'    #specify template 

   def get_queryset(self):
    query = self.request.GET.get('q')
    if query:
        return Ingredient.objects.filter(name__icontains=query)
    else:
        return Ingredient.objects.all()

# def home(request):
#     return render(request, 'ingredients/ingredients_home.html')

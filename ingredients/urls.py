from django.urls import path
from .views import IngredientListView

app_name = 'ingredients'

urlpatterns = [
    path('', IngredientListView.as_view(), name='ingredients_home'),
]

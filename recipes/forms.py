from django import forms
from ingredients.models import Ingredient
from .models import Recipe

CHART_CHOICES = (
    ('pie', 'Pie Chart'),
    ('bar', 'Bar Chart'),
    ('line', 'Line Chart'),
)

#define class-based form imported from django
class SearchForm(forms.Form):
    ingredient = forms.CharField(max_length=100, required=False)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES, required=False)
    
# Form to handle Recipe Data input from the user
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'ingredients', 'pic', 'cooking_time', 'difficulty']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['ingredients'].queryset = Ingredient.objects.all()


from django import forms
from ingredients.models import Ingredient

CHART_CHOICES = (
    ('pie', 'Pie Chart'),
    ('bar', 'Bar Chart'),
    ('line', 'Line Chart'),
)

#define class-based form imported from django
class SearchForm(forms.Form):
    ingredient = forms.CharField(max_length=100, required=False)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES, required=False)
    

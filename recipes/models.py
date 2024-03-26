from django.db import models
from django.urls import reverse

# Create your models here.

difficulty_choices = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard')

)
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    userid = models.ForeignKey('users.User', on_delete=models.CASCADE)
    description = models.TextField()
    ingredients = models.ManyToManyField('ingredients.Ingredient', related_name='recipes')
    cooking_time = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=20, choices=difficulty_choices)
    pic = models.ImageField(upload_to='recipes', default='no_picture.png')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipes:recipe_detail', kwargs={'pk': self.pk})
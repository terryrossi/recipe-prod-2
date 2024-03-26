from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='ingredients', default='no_picture.png')

    
    def __str__(self):
        return self.name
    
   
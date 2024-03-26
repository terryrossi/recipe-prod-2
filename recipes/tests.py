from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from recipes.models import Recipe
from users.models import User
from ingredients.models import Ingredient
from .forms import SearchForm

# Create your tests here.
class RecipeModelTestCase(TestCase):
   
    def setUp(self):
        # Create a User instance
        self.user = User.objects.create(
            username = 'testuser',
            firstname = 'test',
            lastname = 'user',
            email = 'testuser@gmail.com',
            password = 'testpassword'
        )
        # Create an Ingredient instance
        self.ingredient1 = Ingredient.objects.create(name = 'Flour')
        self.ingredient2 = Ingredient.objects.create(name = 'Sugar')

        # Create a Recipe instance
        self.recipe = Recipe.objects.create(
            name = 'Test Recipe',
            userid = self.user,
            description = 'Test Description',
            cooking_time = 30,
            difficulty = 'easy'
        )
        # Add ingredients to the recipe
        self.recipe.ingredients.add(self.ingredient1, self.ingredient2)
        self.recipe.save()

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.name, 'Test Recipe')
        self.assertEqual(self.recipe.userid, self.user)
        self.assertGreater(self.recipe.cooking_time, 0)
        self.assertIn(self.recipe.difficulty, ['easy', 'medium', 'hard'])

    def test_get_absolute_url(self):
       recipe = Recipe.objects.get(id=1)
       #get_absolute_url() should take you to the detail page of recipe #1
       #and load the URL /recipe/1
       self.assertEqual(recipe.get_absolute_url(), '/recipe/1') 

    
class SearchFormTest(TestCase):

    def test_search_form_valid_data(self):
        form = SearchForm(data={
            'ingredient': 'dsvdsvvsd',
            'chart_type': 'pie'
        })
        self.assertTrue(form.is_valid())

    def test_search_form_no_data(self):
        form = SearchForm(data={})
        self.assertTrue(form.is_valid())
      


# class RecipeDetailViewTest(TestCase):

    # @classmethod
    # def setUpTestData(cls):
        # Creating a user for the purpose of creating a recipe
        # cls.user = User.objects.create_user(username='testuser', password='123456')
        # Creating a recipe instance
        # cls.recipe = Recipe.objects.create(
            # name='Sample Recipe',
            # userid=cls.user,
            # description='Sample Description',
            # cooking_time=20,
            # difficulty='easy'
        # )
    
    # def test_redirect_if_not_logged_in(self):
        # Attempting to access the detail view of the created recipe
        # response = self.client.get(reverse('recipes:recipe_detail', args=[self.recipe.pk]))
        # Expected behavior: redirect to the login page
        # self.assertRedirects(response, f'/accounts/login/')

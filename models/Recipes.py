from database import Database
from classes.Recipe import Recipe
import datetime

def get_recipes(selectedCategory):

        '''
        This function returns all the recipes in the database
        
        '''
        db = Database(users=[], categories=[], recipes=[], ingredients=[])
        recipes = db.get_recipes()
        recipes_by_category = []

        for recipe in recipes:
                if (recipe["category"] == selectedCategory):
                        recipes_by_category.append(recipe)
                if(selectedCategory == "All Recipes"):
                        return recipes

        return recipes_by_category

def get_recipe_by_id(recipe_id):

        '''
        This function returns a recipe by its id
        
        '''
        db = Database(users=[], categories=[], recipes=[], ingredients=[])
        recipes = db.get_recipes()

        for recipe in recipes:
                if (recipe["id"] == recipe_id):
                        return recipe

        return None

def get_recipes_by_date(recipes):

        '''
        This function will sort the recipes by date
        '''
        recipes_by_date = []

        for recipe in recipes:
               # get the current recipes date
                recipe_date = recipe["createdAt"]

                # get the recipes from the last 3 mouths
                last_3_mouths = datetime.datetime.now() - datetime.timedelta(days=90) ## timedelta allows to opperate with dates

                # convert the recipe date to datetime
                recipe_date = datetime.datetime.strptime(recipe_date, "%d/%m/%Y")
                
                # check if the recipe date is greater than the last 3 mouths

                if (recipe_date > last_3_mouths):
                        recipes_by_date.append(recipe)

        return recipes_by_date
                
  

def get_logged_user_recipes(recipes, logged_user):

        '''
        This function will return the recipes of the logged user (username)
        '''
        user_recipes = []

        for recipe in recipes:
                if (recipe["creator"] == logged_user):
                        user_recipes.append(recipe)

        return user_recipes

def get_recipes_by_ingredient(recipes, ingredient):

        '''
        This function will return the recipes by ingredient
        '''
        db = Database(users=[], categories=[], recipes=[], ingredients=[])

        db_ingredients = db.get_ingredients()

        recipes_by_ingredient = []

        # joining the recipes with the ingredients
        for recipe in recipes:
         for db_ingredient in db_ingredients:
                if (recipe["id"] == db_ingredient["recipeID"]):
                        if (ingredient.lower() in db_ingredient["ingredient"].lower()):
                                recipes_by_ingredient.append(recipe)
                     
        return recipes_by_ingredient

def canUserEdit(logged_user, recipe_id):

        '''
        This function will check if the logged user can edit the recipe each means change or delete it
        '''
        db = Database(users=[], categories=[], recipes=[], ingredients=[])

        recipes = db.get_recipes()

        for recipe in recipes:
                if (recipe["id"] == recipe_id):
                        if (recipe["creator"] == logged_user):
                                return True

        return False

def create_recipe(recipe):

        '''
        This function will create a new recipe
        '''
        recipe = Recipe(recipe["id"], recipe["createdAt"], recipe["category"], recipe["creator"], recipe["title"], recipe["prepMode"], recipe["estimatedTime"], recipe["image"], recipe["views"])

        recipe.create_recipe(recipe)

def update_title(recipe):
        
                '''
                This function will update the title of a recipe
                '''
                recipe = Recipe(recipe["id"], recipe["createdAt"], recipe["category"], recipe["creator"], recipe["title"], recipe["prepMode"], recipe["estimatedTime"], recipe["image"], recipe["views"])
        
                recipe.update_recipe_title(recipe)

def update_views(recipe):
                
  '''
This function will update the views of a recipe
'''
  recipe = Recipe(recipe["id"], recipe["createdAt"], recipe["category"], recipe["creator"], recipe["title"], recipe["prepMode"], recipe["estimatedTime"], recipe["image"], recipe["views"])
        
  recipe.update_recipe_views(recipe) 

def delete_recipe(recipe):
                                
                '''
                This function will delete a recipe
                '''
                recipe = Recipe(recipe["id"], recipe["createdAt"], recipe["category"], recipe["creator"], recipe["title"], recipe["prepMode"], recipe["estimatedTime"], recipe["image"], recipe["views"])
        
                recipe.delete_recipe(recipe)

def count_views(recipe_id):

        '''
        This function will count the views of a recipe
        '''
        db = Database(users=[], categories=[], recipes=[], ingredients=[])

        recipes = db.get_recipes()

        for recipe in recipes:
                if (recipe["id"] == recipe_id):
                        recipe["views"] += 1
                        recipe = Recipe(recipe["id"], recipe["createdAt"], recipe["category"], recipe["creator"], recipe["title"], recipe["prepMode"], recipe["estimatedTime"], recipe["image"], recipe["views"])
                        recipe.update_recipe_views(recipe)
                        return recipe["views"]

        return None

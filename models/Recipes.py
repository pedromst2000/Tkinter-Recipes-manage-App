from database import Database
from classes.Recipe import Recipe
import time

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

                # convert the date to a timestamp     
                recipe_date = time.strptime(recipe_date, "%d/%m/%Y")
                recipe_date = time.mktime(recipe_date)
                 
                        # append the recipe to the list
                recipes_by_date.append(recipe)
                 
                        # sort the list by date without lambda
                recipes_by_date.sort(key=lambda x: x["createdAt"], reverse=True ) # sort the list by date with lambda (anonymous function)
             
                 
        return recipes_by_date


def get_recipes_by_views(recipes, views):

        '''
        This function will return the recipes by views
        '''

        recipes_by_views = []

        for recipe in recipes:
                if (recipe["views"] == views):
                        recipes_by_views.append(recipe)

        return recipes_by_views       


def get_recipes_by_title(recipes, title):
                
                '''
                This function will filter the recipes by title
                '''

                recipes_by_title = []

                for recipe in recipes:
                        if (recipe["title"] == title):
                                recipes_by_title.append(recipe)


                return recipes_by_title


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
                                if (db_ingredient["ingredient"] == ingredient):
                                        recipes_by_ingredient.append(recipe)

        return recipes_by_ingredient
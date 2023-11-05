from database import Database
from classes.Recipe import Recipe


def get_recipes():
    
        '''
        This function returns all the recipes in the database
        '''
    
        db = Database(users=[], categories=[], recipes=[])
        recipes = db.get_recipes()
        return recipes
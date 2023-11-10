from database import Database
from classes.Category import Category


def get_categories():

    '''
    This function returns all the categories in the database
    '''

    db = Database(users=[], categories=[], recipes=[], ingredients=[])
    categories = db.get_categories()
    return categories


def create_category(category):

    '''
    This function creates a new category and returns True if the category was created
    '''

    category = Category(category)
    category.add_category()

    return True


def delete_category(category):

    '''
    This function deletes a category and returns True if the category was deleted
    '''

    category = Category(category)
    category.delete_category()

    return True


def checkCategory(_category_):

    '''
    This function checks if the category is unique and returns True if the category is unique and False if the category is not unique
    '''

    db = Database(users=[], categories=[], recipes=[], ingredients=[])
    categories = db.get_categories()
    print(categories)

    for category in categories:
        if category["category"] == _category_:
            return True
    
    return False # if the category is not in the database
from database import Database
from classes.Category import Category


def get_categories():

    '''
    This function returns all the categories in the database
    '''

    db = Database(users=[], categories=[])
    categories = db.get_categories()
    return categories


def create_category(tag, category):

    '''
    This function creates a new category and returns True if the category was created
    '''

    category = Category(tag, category)
    category.add_category()

    return True


def delete_category(tag, category):

    '''
    This function deletes a category and returns True if the category was deleted
    '''

    category = Category(tag, category)
    category.delete_category()

    return True

def checkTag(tag):

    '''
    This function checks if the tag is unique and returns True if the tag is unique and False if the tag is not unique
    '''

    db = Database(users=[], categories=[])
    categories = db.get_categories()

    for category in categories:
        if category["tag"] == tag:
            return True
        
    return False # if the tag is not in the database

def checkCategory(_category_):

    '''
    This function checks if the category is unique and returns True if the category is unique and False if the category is not unique
    '''

    db = Database(users=[], categories=[])
    categories = db.get_categories()
    print(categories)

    for category in categories:
        if category["name"] == _category_:
            return True
    
    return False # if the category is not in the database
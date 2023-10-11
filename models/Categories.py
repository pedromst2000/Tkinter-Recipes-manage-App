from database import Database
from classes.Category import Category


def get_categories():
    db = Database(users=[], categories=[])
    categories = db.get_categories()
    return categories


def create_category(tag, category):
    category = Category(tag, category)
    category.add_category()

    return True


def delete_category(tag, category):
    category = Category(tag, category)
    category.delete_category()

    return True


# # checking if the Tag is unique
def checkTag(tag):
    db = Database(users=[], categories=[])
    categories = db.get_categories()

    for category in categories:
        if category["tag"] == tag:
            return True
        
    return False # if the tag is not in the database

# checking if the category is unique
def checkCategory(_category_):
    db = Database(users=[], categories=[])
    categories = db.get_categories()
    print(categories)

    for category in categories:
        if category["name"] == _category_:
            return True
    
    return False # if the category is not in the database
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

    tags = [category["tag"] for category in categories]

    if tag in tags:
        return True
    else:
        return False

# checking if the category is unique
def checkCategory(_category_):
    db = Database(users=[], categories=[])
    categories = db.get_categories()

    categories = [category["name"].lower() for category in categories]


    if _category_.lower() in categories:
        return True
    else:
        return False


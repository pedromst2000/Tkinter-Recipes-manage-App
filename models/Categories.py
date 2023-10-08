from database import Database
from classes.Category import Category


def get_categories():
    db = Database(users=[], categories=[])
    categories = db.get_categories()
    return categories


def create_category(tag, category):
    category = Category(tag, category)
    category.add_category()


def delete_category(tag, category):
    category = Category(tag, category)
    category.delete_category()
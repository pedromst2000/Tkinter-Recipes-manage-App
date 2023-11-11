from database import Database

class Recipe:

    # attributes
    TAG = ""
    creator = ""
    title = ""
    prepMode = ""
    estimatedTime = ""
    image = ""
    views = 0  


    # constructor
    def __init__(self, TAG, creator, title, prepMode, estimatedTime, image, views):
        self.TAG = TAG
        self.creator = creator
        self.title = title
        self.prepMode = prepMode
        self.estimatedTime = estimatedTime
        self.image = image
        self.views = views

    # methods
    def create_recipe(self, recipe):
            db = Database(users=[], categories=[], recipes=[], ingredients=[])
            db.create_recipe(recipe)

    def update_recipe_title(self, recipe):
                db = Database(users=[], categories=[], recipes=[], ingredients=[])
                db.update_recipe(recipe)

    def update_recipe_views(self, recipe):
                db = Database(users=[], categories=[], recipes=[], ingredients=[])
                db.update_recipe(recipe)

    def delete_recipe(self, recipe):
                db = Database(users=[], categories=[], recipes=[], ingredients=[])
                db.delete_recipe(recipe)


    
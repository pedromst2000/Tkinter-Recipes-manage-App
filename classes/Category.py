from database import Database

class Category:
    
        # attributes
        category = ""
    
        # constructor
        def __init__(self, category):
            self.category = category

        # methods
        # add new instance of the Class Category
        def add_category(self):
            db = Database(users=[],categories=[], recipes=[], ingredients=[]) 
            db.create_category(self)
       
        # delete an instance of the Class Category
        def delete_category(self):
            db = Database(users=[],categories=[], recipes=[], ingredients=[])
            db.delete_category(self)
from database import Database

class Category:
    
        # attributes
        tag = ""
        category = ""
    
        # constructor
        def __init__(self, tag, category):
            self.tag = tag
            self.category = category
    
        # methods
        # add new instance of the Class Category
        def add_category(self):
            db = Database(users=[],categories=[]) 
            db.create_category(self)
       
        # delete an instance of the Class Category
        def delete_category(self):
            db = Database(users=[],categories=[])
            db.delete_category(self)
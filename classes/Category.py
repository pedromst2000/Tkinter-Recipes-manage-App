from database import Database

class Category:
    
        # attributes
        tag = ""
        name = ""
    
        # constructor
        def __init__(self, tag, name):
            self.tag = tag
            self.name = name
    
        # methods
        # add new instance of the Class Category
        def add_category(self):
            db = Database(users=[],categories=[]) 
            db.create_category(self)
       
        # delete an instance of the Class Category
        def delete_category(self):
            db = Database(users=[],categories=[])
            db.delete_category(self)
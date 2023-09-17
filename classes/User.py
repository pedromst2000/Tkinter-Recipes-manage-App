from database import Database

class User:

    # attributes
    username = ""
    email = ""
    password = ""
    role = ""
    isBlocked = False


    # constructor
    def __init__(self, username, email, password, role, isBlocked):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.isBlocked = isBlocked

    # methods
    # def add_user(self):
    #     db = Database()
    #     db.add_user(self)
    
    # def update_user(self):
    #     db = Database()
    #     db.update_user(self)
    
    # def delete_user(self):
    #     db = Database()
    #     db.delete_user(self)

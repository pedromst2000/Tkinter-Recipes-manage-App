from database import Database

class User:

    # attributes
    username = ""
    email = ""
    password = ""
    role = ""
    avatar = ""
    isBlocked = False


    # constructor
    def __init__(self, username, email, password, role, avatar, isBlocked):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.avatar = avatar
        self.isBlocked = isBlocked

    # methods
    # add new instance of the Class User
    def add_user(self):
        db = Database(users=[], categories=[], recipes=[], ingredients=[]) 
        db.create_user(self)

    # update an instance of the Class User    
    def update_user(self):
        db = Database(users=[], categories=[], recipes=[], ingredients=[])
        db.update_user(self)
    
    # delete an instance of the Class User
    def delete_user(self):
        db = Database(users=[], categories=[], recipes=[], ingredients=[])
        db.delete_user(self)

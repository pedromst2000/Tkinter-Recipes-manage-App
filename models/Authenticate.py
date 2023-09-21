from database import Database
from classes.User import User
from database import *


def login(email, password):

    # the class Database takes a list of users as a parameter since the constructor takes a list of users as a parameter (self, users)
    db = Database(users=[])
    users = db.get_users()

    for user in users:
        # check if the email exists
        if user["email"] == email:
            # check if the password is correct
            if user["password"] == password:
                return user
            else:
                return None # if the password is incorrect, return None
 
    return None # if the email doesn't exist, return None


# this function will check the logged user role 
def checkLoggedUserRole(email):
    db = Database(users=[]) 
    users = db.get_users()

    for user in users:
        if user["email"] == email: # if the email exists in the database
            return user["role"] # return the role of the user

    return None # if the email doesn't exist in the database, return None

# this function will check if the logged user is blocked
def checkLoggedUserIsBlocked(email):
    db = Database(users=[])
    users = db.get_users()

    for user in users:
        if user["email"] == email: # if the email exists in the database
            return user["isBlocked"] # return the isBlocked value of the user

    return None # if the email doesn't exist in the database, return None



def register(username, email, password):
    
        db = Database(users=[])
        users = db.get_users()
    
        for user in users:
            if user["email"] == email:  # check if the email already exists

                return False
            if user["username"] == username: # check if the username already exists
                return False
    
        # if the email and the username doesn't exist, create the user
        user = User(username, email, password, "regular", False)
        user.add_user()
    
        return True # return True if the user was created successfully
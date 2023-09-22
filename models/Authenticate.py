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
                return None  # if the password is incorrect, return None

    return None  # if the email doesn't exist, return None


# this function will check the logged user role
def checkLoggedUserRole(email):
    db = Database(users=[])
    users = db.get_users()

    for user in users:
        if user["email"] == email:  # if the email exists in the database
            return user["role"]  # return the role of the user

    return None  # if the email doesn't exist in the database, return None



# this function will check if the logged user is blocked


def checkLoggedUserIsBlocked(email):
    db = Database(users=[])
    users = db.get_users()

    for user in users:
        if user["email"] == email:  # if the email exists in the database
            return user["isBlocked"]  # return the isBlocked value of the user

    return None  # if the email doesn't exist in the database, return None


# add a new user to the database
def register(username, email, password):

    # if the email and the username doesn't exist, create the user
    user = User(username, email, password, "regular",
                "assets/images/avatar_profile_placeholder.jpg",
                False)
    user.add_user()

    return True  # return True if the user was created successfully


# check if the username is unique
def checkRegisterUsername(username):
    db = Database(users=[])
    users = db.get_users()

    username = username.lower()  # to make the username case insensitive

    for user in users:
        if user["username"].lower() == username:
            return False

    return True

# check if the email is unique


def checkRegisterEmail(email):
    db = Database(users=[])
    users = db.get_users()

    # make the first part of the email case insensitive
    # split the email by @ -> eg: email = ["john", "gmail.com"]
    email = email.split("@")
    # make the first part of the email case insensitive -> eg: email = ["john", "gmail.com"] -> email = ["john", "gmail.com"]
    email[0] = email[0].lower()

    # join the email back -> eg: email = ["john", "gmail.com"] -> email = "john@gmailcom"
    email = "@".join(email)

    for user in users:
        if user["email"].lower() == email:
            return False

    return True  # if the email is unique, return True

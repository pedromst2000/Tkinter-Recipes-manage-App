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
                return None

    return None


def checkLoggedUserRole(email):
    db = Database(users=[])
    users = db.get_users()

    for user in users:
        if user["email"] == email:
            return user["role"]

    return None


def checkLoggedUserIsBlocked(email):
    db = Database(users=[])
    users = db.get_users()

    for user in users:
        if user["email"] == email:
            return user["isBlocked"]

    return None


# def register(username, email, password):
#     # register the user in the database with the role by default "regular"
#     db = Database()
#     user = {
#         "username": username,
#         "email": email,
#         "password": password,
#         "role": "regular",
#         "isBlocked": False
#     }

#     # check if the user already exists
#     # if the user exists, return None
#     users = db.get_users()
#     for user in users:
#         if user["email"] == email:
#             return None

#         if user["username"] == username:
#             return None

#     # add the instance of the user to the database
#     User(username, email, password, "regular", False).add_user()

#     return user

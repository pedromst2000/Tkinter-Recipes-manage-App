from database import Database
from classes.User import User
from database import *


def login():

    db = Database(users=[]) # the class Database takes a list of users as a parameter since the constructor takes a list of users as a parameter (self, users)
    users = db.get_users()

    print(users)


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

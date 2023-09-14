from database import Database
from classes.User import User


def login(email, password):
    db = Database()
    users = db.get_users()
    for user in users:
        if user["email"] == email and user["password"] == password:
            return user
    return None


def register(username, email, password):
    # register the user in the database with the role by default "regular"
    db = Database()
    user = {
        "username": username,
        "email": email,
        "password": password,
        "role": "regular",
        "isBlocked": False
    }

    # check if the user already exists
    # if the user exists, return None
    users = db.get_users()
    for user in users:
        if user["email"] == email:
            return None

        if user["username"] == username:
            return None

    # add the instance of the user to the database
    User(username, email, password, "regular", False).add_user()

    return user

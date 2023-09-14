import csv
import os
from typing import Optional, Any, Dict

DELIMITER = ";"

USERS_FIELDS = ["username", "email", "password", "role", "isBlocked"]
USERS_CSV_PATH = os.path.join(os.path.dirname(
    __file__), "..", "database", "users.csv")

# columns indexes
USERS_ID_INDEX = 0
USERS_USERNAME_INDEX = 1
USERS_EMAIL_INDEX = 2
USERS_PASSWORD_INDEX = 3
USERS_ROLE_INDEX = 4
USERS_IS_BLOCKED_INDEX = 5


# THERE ARE ONLY THE USERS METHODS FOR NOW !!

class Database:

    def __init__(self):
        pass

    def read_users(self) -> list:
        users = []
        with open(USERS_CSV_PATH, "r") as users_csv:
            reader = csv.reader(users_csv, delimiter=DELIMITER)
            for row in reader:
                users.append(row)
        return users

    def write_users(self, users: list):
        with open(USERS_CSV_PATH, "w") as users_csv:
            writer = csv.writer(users_csv, delimiter=DELIMITER)
            writer.writerows(users)

    def get_user_by_id(self, id: int) -> Optional[Dict[str, Any]]:
        users = self.read_users()
        for user in users:
            if user[USERS_ID_INDEX] == str(id):
                return {
                    "id": user[USERS_ID_INDEX],
                    "username": user[USERS_USERNAME_INDEX],
                    "email": user[USERS_EMAIL_INDEX],
                    "password": user[USERS_PASSWORD_INDEX],
                    "role": user[USERS_ROLE_INDEX],
                    "isBlocked": user[USERS_IS_BLOCKED_INDEX]
                }
        return None

    def get_users(self) -> list:
        users = self.read_users()

    def add_user(self, user: dict):
        users = self.read_users()
        users.append([
            str(len(users) + 1),
            user["username"],
            user["email"],
            user["password"],
            user["role"],
            user["isBlocked"]
        ])
        self.write_users(users)

    def update_user(self, user: dict):
        users = self.read_users()
        for index, row in enumerate(users):
            if row[USERS_ID_INDEX] == user["id"]:
                users[index] = [
                    user["id"],
                    user["username"],
                    user["email"],
                    user["password"],
                    user["role"],
                    user["isBlocked"]
                ]
                break
        self.write_users(users)

    def delete_user(self, id: int):
        users = self.read_users()
        for index, row in enumerate(users):
            if row[USERS_ID_INDEX] == str(id):
                del users[index]
                break
        self.write_users(users)

    def get_user_by_id(self, id: int) -> Optional[Dict[str, Any]]:
        users = self.read_users()
        for user in users:
            if user[USERS_ID_INDEX] == str(id):
                return {
                    "id": user[USERS_ID_INDEX],
                    "username": user[USERS_USERNAME_INDEX],
                    "email": user[USERS_EMAIL_INDEX],
                    "password": user[USERS_PASSWORD_INDEX],
                    "role": user[USERS_ROLE_INDEX],
                    "isBlocked": user[USERS_IS_BLOCKED_INDEX]
                }
        return None
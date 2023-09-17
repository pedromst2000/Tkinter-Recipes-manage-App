import csv
import os
from typing import Optional, Any, Dict

DELIMITER = ";"

USERS_FIELDS = ["username", "email", "password", "role", "isBlocked"]
USERS_CSV_PATH = os.path.join(os.path.dirname(
    __file__),  "database", "users.csv")


# THERE ARE ONLY THE USERS METHODS FOR NOW !!

class Database:

    def __init__(self):
        pass

    def get_users(self) -> list:
        users = []
        with open(USERS_CSV_PATH, "r") as users_csv:
            reader = csv.DictReader(users_csv, delimiter=DELIMITER)
            for row in reader:
                users.append(row)
        return users

    def get_user(self, email: str) -> Optional[Dict[str, Any]]:
        users = self.get_users()
        for user in users:
            if user["email"] == email:
                return user
        return None

    def add_user(self, user: Dict[str, Any]) -> None:
        with open(USERS_CSV_PATH, "a") as users_csv:
            writer = csv.DictWriter(
                users_csv, fieldnames=USERS_FIELDS, delimiter=DELIMITER)
            writer.writerow(user)

    def update_user(self, user: Dict[str, Any]) -> None:
        users = self.get_users()
        for index, _user in enumerate(users):
            if _user["email"] == user["email"]:
                users[index] = user
                break
        with open(USERS_CSV_PATH, "w") as users_csv:
            writer = csv.DictWriter(
                users_csv, fieldnames=USERS_FIELDS, delimiter=DELIMITER)
            writer.writeheader()
            writer.writerows(users)

    def delete_user(self, user: Dict[str, Any]) -> None:
        users = self.get_users()
        for index, _user in enumerate(users):
            if _user["email"] == user["email"]:
                del users[index]
                break
        with open(USERS_CSV_PATH, "w") as users_csv:
            writer = csv.DictWriter(
                users_csv, fieldnames=USERS_FIELDS, delimiter=DELIMITER)
            writer.writeheader()
            writer.writerows(users)

    

    



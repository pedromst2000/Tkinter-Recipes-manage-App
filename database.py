from utils import increment_id

class Database:

    users = []
    # recipes = []
    # favorites = []
    # comments = []

# constructor
    def __init__(self,
                 users,
                #   recipes,
                #   favorites,
                #     comments
                 ):
        self.users = users
        # self.recipes = recipes
        # self.favorites = favorites
        # self.comments = comments

# methods
    def get_users(self):

        file = open("database/users.txt", "r", encoding="utf-8")

        lines = file.readlines()

        for line in lines:
            user = line.split(";")
            self.users.append({
                "id": int(user[0]),
                "username": user[1],
                "email": user[2],
                "password": user[3],
                "role": user[4],
                "avatar": user[5],
                # to check if the user is blocked or not
                "isBlocked": (user[6]).strip("\n").replace(" ", "") == "True"
            })


        file.close()

        return self.users

      

    # to check the type of the data in the list
        # print(
        #     type(self.users[0]["id"]),
        #     type(self.users[0]["username"]),
        #     type(self.users[0]["email"]),
        #     type(self.users[0]["password"]),
        #     type(self.users[0]["role"]),
        #     type(self.users[0]["avatar"]),
        #     type(self.users[0]["isBlocked"])
        # )

      
    def create_user(self, user):  # add a new user to the database
        file = open("database/users.txt", "a", encoding="utf-8")

        file.write(
            f"\n{increment_id()};{user.username};{user.email};{user.password};{user.role};{user.avatar};{user.isBlocked}")

        file.close()

    def update_user(self, user):


        file = open("database/users.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("database/users.txt", "w+", encoding="utf-8")

        for line in lines:
            if line.split(";")[0] != str(user.id): # if the id of the user is not the same as the id of the user in the line
                file.write(line) # write the line as it is
            else:
                file.write(
                    f"{user.id};{user.username};{user.email};{user.password};{user.role};{user.avatar};{user.isBlocked}\n")

        file.close()

    def delete_user(self, user):
        file = open("database/users.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("database/users.txt", "w+", encoding="utf-8")

        for line in lines:
            if line.split(";")[0] != str(user.id):
                file.write(line)

        file.close()
class Database:

    users = []
    # recipes = []
    # favorites = []
    # comments = []

# constructor
    def __init__(self, 
                 users, 
                #  recipes, 
                #  favorites,
                #    comments
                 ):
        self.users = users
        # self.recipes = recipes
        # self.favorites = favorites
        # self.comments = comments

# methods
    def get_users(self):

        file = open("database/users.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        for line in lines:
            user = line.split(";")
            self.users.append({
                "id": int(user[0]),
                "username": user[1],
                "email": user[2],
                "password": user[3],
                "role": user[4],
                "isBlocked": (user[5]).strip("\n").replace(" ", "") == "true" # to check if the user is blocked or not 
            })

    
    # to check the type of the data in the list 
        # print(
        #     type(self.users[0]["id"]),
        #     type(self.users[0]["username"]),
        #     type(self.users[0]["email"]),
        #     type(self.users[0]["password"]),
        #     type(self.users[0]["role"]),
        #     type(self.users[0]["isBlocked"])
        # )

        return self.users
    

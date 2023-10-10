
class Database:

    users = []
    categories = []
    # recipes = []
    # favorites = []
    # comments = []

# constructor
    def __init__(self,
                 users,
                 categories
                 #   recipes,
                 #   favorites,
                 #     comments
                 ):
        self.users = users
        self.categories = categories
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
                "username": user[0],
                "email": user[1],
                "password": user[2],
                "role": user[3],
                "avatar": user[4],
                # to check if the user is blocked or not
                "isBlocked": (user[5]).strip("\n").replace(" ", "") == "True"
            })

        file.close()

        return self.users

    def get_categories(self):
            
            file = open("database/categories.txt", "r", encoding="utf-8")
    
            lines = file.readlines()
    
            for line in lines:
                category = line.split(";")
                self.categories.append({
                    "tag": category[0],
                    "name": category[1],
                })

            file.close()

            return self.categories

    def create_user(self, user):  # add a new user to the database
       
       file = open("database/users.txt", "a", encoding="utf-8")

       file.write(
            f"{user.username};{user.email};{user.password};{user.role};{user.avatar};{user.isBlocked}\n")
       
       file.close()
       
    def create_category(self, category):  # add a new category to the database
        
       file = open("database/categories.txt", "a", encoding="utf-8")

       file.write(
            f"{category.tag};{category.name}\n")
       
       file.close()

    def update_user(self, user):

        file = open("database/users.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("database/users.txt", "w+", encoding="utf-8")

        for line in lines:
            # upddate by the email or username
            if line.split(";")[0] == user.username or line.split(";")[1] == user.email:
                file.write(
                    f"{user.username};{user.email};{user.password};{user.role};{user.avatar};{user.isBlocked}\n")
            else:
                file.write(line)

        file.close()

    def delete_user(self, user):

        file = open("database/users.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("database/users.txt", "w+", encoding="utf-8")

        for line in lines:
            if line.split(";")[0] != user.username and line.split(";")[1] != user.email:
                file.write(line)

        file.close()                
       
    def delete_category(self, category):
            
            file = open("database/category.txt", "r", encoding="utf-8")
    
            lines = file.readlines()
    
            file.close()
    
            file = open("database/category.txt", "w+", encoding="utf-8")
    
            for line in lines:
                if line.split(";")[0] != category.tag and line.split(";")[1] != category.name:
                    file.write(line)
    
            file.close()
    
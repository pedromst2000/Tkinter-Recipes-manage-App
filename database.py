
class Database:

    users = []
    categories = []
    recipes = []
    ingredients = []
    # favorites = []
    # comments = []


# constructor
    def __init__(self,
                 users,
                 categories,
                 recipes,
                ingredients  
                #   favorites,
                 #     comments,
                 ):
        self.users = users
        self.categories = categories
        self.recipes = recipes
        self.ingredients = ingredients
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
                "category": category[0].strip("\n"),
            })

        file.close()

        return self.categories

    def get_recipes(self):

        file = open("database/recipes.txt", "r", encoding="utf-8")

        lines = file.readlines()

        for line in lines:
            recipe = line.split(";")
            self.recipes.append({
                "id": int(recipe[0]),
                "createdAt": recipe[1],
                # TAG => is the category associated with the recipe
                "category": recipe[2],
                "creator": recipe[3],
                "title": recipe[4],
                # prepMode => is the preparation mode of the recipe
                "prepMode": recipe[5],
                # estimatedTime => is the estimated time to prepare the recipe (confection time)
                "estimatedTime": int(recipe[6]),
                "image": recipe[7],
                "views": int(recipe[8].strip("\n"))
            })

        file.close()

        return self.recipes

    def get_ingredients(self):

        file = open("database/ingredients.txt", "r", encoding="utf-8")

        lines = file.readlines()

        for line in lines:
            ingredient = line.split(";")
            self.ingredients.append({
                "recipeID": int(ingredient[0]),
                "ingredient": ingredient[1].strip("\n")
            })

        file.close()

        return self.ingredients

    def create_user(self, user):  # add a new user to the database

        file = open("database/users.txt", "a", encoding="utf-8")

        file.write(
            f"{user.username};{user.email};{user.password};{user.role};{user.avatar};{user.isBlocked}\n")

        file.close()

    def create_category(self, category):  # add a new category to the database

        file = open("database/categories.txt", "a", encoding="utf-8")

        file.write(
            f"{category.category}\n")

        file.close()

    def create_recipe(self, recipe):  # add a new recipe to the database
            
            file = open("database/ingredients.txt", "a", encoding="utf-8")

            for ingredient in recipe.ingredients:
                file.write(
                    f"{recipe.id};{ingredient}\n")
            
            file.close()

            file = open("database/recipes.txt", "a", encoding="utf-8")

            file.write(
                f"{recipe.id};{recipe.createdAt};{recipe.category};{recipe.creator};{recipe.title};{recipe.prepMode};{recipe.estimatedTime};{recipe.image};{recipe.views}\n")
            
            file.close()

    def update_recipe(self, recipe):  
        file = open("database/recipes.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("database/recipes.txt", "w+", encoding="utf-8")

        for line in lines:

            if line.split(";")[0] == recipe.id:
                file.write(
                    f"{recipe.id};{recipe.createdAt};{recipe.category};{recipe.creator};{recipe.title};{recipe.prepMode};{recipe.estimatedTime};{recipe.image};{recipe.views}\n")
            else:
                file.write(line)

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

        file = open("database/categories.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("database/categories.txt", "w+", encoding="utf-8")

        for line in lines:
            if line.split(";")[0] != category.category:
                file.write(line)

        file.close()

    def delete_recipe(self, recipe):

        file = open("database/recipes.txt", "r", encoding="utf-8")

        lines = file.readlines()

        file.close()

        file = open("database/recipes.txt", "w+", encoding="utf-8")

        for line in lines:
            if line.split(";")[0] != recipe.id:
                file.write(line)

        file.close()


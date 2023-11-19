User Stories - Requirements - Features

-- Improve the documentation of the Tkinter App

-- In the end refactor the code (remove unecessary code) => Refactor

-- Docstring for the functions => Refactor

-- Add new branch for second version of the app

-- add validation for the title of the recipe -min 20char -max 45char => Feature

--!! Add Recipe Image Feature !!-- => Feature
* add the image from other device to the directory of the app with the follow pattern name_of_the_recipe.jpg
* lower case and replace spaces with underscore

-- to be done in the next commits

- [X]  The users authenticate on the app with their account : email and password (login)
- [X]  if the user doesn't have an account, he can sign up with the following information: username, email and password 
- [X] The user can acess the sign up page trought 'link' that will open the sign up window and close the login window 
- [X]  The user can acess the login page trought 'link' that will open the login window and close the sign up window 
- [X]  The user can acess aswell the login page through the navbar
- [X]  The user can acess aswell the sign up page through the navbar
- [X]  The username should be unique
- [X]  The email should be unique
- [X]  In the login or in the register the password field should have hidden or visible password option
- [X]  New user should have dummy profile picture
- [X]  A logged User can acess to his profile page
- [X]  The users should have two roles: regular and admin
- [X]  Only the admin can manage the categories of the recipes (add or delete categories of recipes)
- []  Only the admin can manage the regular users
- []  Only the admin can configure the notifications
- [X]  The admin should have a list of the categories of the recipes wich should be dynamic (add or delete categories of recipes)
- [X]  The regular user should have the possibility to edit his profile (change password, change avatar)
- [X]  The regular user should have the possibility to delete his account on his profile page
- []  An user should be able to add recipes to the catalog
- []  An user should be able to delete his own recipes
- [X]  A recipe should have atleast : title, preparation mode, estimated time of confection, image of the recipe, ingredients, category of the recipe (can have more than one category)
- [x]  A recipe should be associated atleast to one category
- []  An user can add , delete and edit his own recipes (only the owner of the recipe can edit or delete the recipe)
- []  When the user add a recipe should be pending for approval of the admin
- []  The admin should have a list with the recipes pending for approval in his profile (should be able to approve or delete the recipe)
- []  When the admin approve the recipe, the recipe should be available on the catalog
- []  An user can create a list of his favorite recipes
- []  In the user profile should be available the categories of the recipes that most interest the user to receive notifications (eg: 
    in the list contains the category dessert, the user should receive notifications of new recipes of the category dessert
)
- []  The user should be able to receive notifications of his favorite recipes when a new recipe is added to the catalog
- [X]  The application should apresent the catalog of the recipes to the user (should apresent by default the most recent recipes)
- [X]  The user should be able to filter the recipes by category
- [X]  The user should be able to filter the recipes by title
- [X]  The user should be able to filter the recipes by specific ingredient
- []  The user should be able to filter the recipes by views --
- []  The catalog should be sorted by the number of views of the recipe for instance --
- []  An user can comment a recipe , by creating thread of comments (can have more than one comment of other users)
- []  An user can like a recipe
- []  The app should have a dashboard (painel) with the total recipes, total recipes by category
- []  The admin should have a list of the users of the app (should be able to block user in case of inappropriate behavior eg: bad comments, bad recipes with inappropriate content) 
- []  A blocked user should be hable to read the guidelines of the app
- []  A blocked user should be hable to see the blocked time (eg: 1 week, 1 month, 1 year)

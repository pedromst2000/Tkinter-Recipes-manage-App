from tkinter import messagebox, Tk, Frame, TOP, X, NW, Canvas, Image, Button, Toplevel, ttk, Listbox
from PIL import ImageTk, Image
from classes.Navbar import NavbarWidget
from models.Recipes import *


def RecipesCatalogView(selectedCategory, user, RecipesCategoryWindow):

    RecipesCatalogWindow = Toplevel(RecipesCategoryWindow)

    # hide the main window
    RecipesCategoryWindow.withdraw()

    RecipesCatalogWindow.title("CraftingCook - Recipes")

    RecipesCatalogWindow.geometry("1280x650")

    RecipesCatalogWindow.iconbitmap("assets/CraftingCook.ico")

    RecipesCatalogWindow.resizable(0, 0)

    navbar = NavbarWidget(
        RecipesCatalogWindow, 
        "assets/images/Home/notification.png", # notificationIcon
        "assets/images/Home/exit_app.png", # exitAppIcon
        user
    )

    navbar.create_widget()

    canvasRecipesCatalog = Canvas(RecipesCatalogWindow, height=650, width=1280)
    canvasRecipesCatalog.place(x=-2, y=100)

    image = Image.open("assets/images/Recipes/Recipes_Catalog_Background.png")
    image = image.resize((1280, 650))

    image = ImageTk.PhotoImage(image)

    canvasRecipesCatalog.create_image(0, 0, anchor=NW, image=image)

    recipes = get_recipes(selectedCategory)
    default_recipes = get_recipes_by_date(recipes)
    
    inputSearch = ttk.Entry(canvasRecipesCatalog, width=35 , foreground="#B5960E", font=("Arial", 10, "bold") )
    inputSearch.place(x=50, y=50)

    inptutSearchIngredient = ttk.Entry(canvasRecipesCatalog, width=35 , foreground="#B5960E", font=("Arial", 10, "bold"))
    inptutSearchIngredient.place(x=460, y=50)

    btnSearch = Button(canvasRecipesCatalog, text="Search", font=("Arial", 12, "bold"), bg="#B5960E", fg="white",  cursor="hand2", width=8, height=2, activebackground="#D1A711", activeforeground="#ffffff", bd=0)
    btnSearch.place(x=320, y=36)

    btnSearchIngredient = Button(canvasRecipesCatalog, text="Search Ingredient", font=("Arial", 12, "bold"), bg="#B5960E", fg="white",  cursor="hand2", width=14, height=2, activebackground="#D1A711", activeforeground="#ffffff", bd=0)
    btnSearchIngredient.place(x=720, y=36)
    
    # treeview to display the recipes with columns title category views data
    recipesList = ttk.Treeview(canvasRecipesCatalog, columns=("title", "category", "views", "created date"), show="headings", height=20)
    
    recipesList.heading("title", text="Title")
    recipesList.heading("category", text="Category")
    recipesList.heading("views", text="Views")
    recipesList.heading("created date", text="Created Date")

    recipesList.column("title", width=280)
    recipesList.column("category", width=120, anchor="center")
    recipesList.column("views", width=100, anchor="center")
    recipesList.column("created date", width=120, anchor="center")
    
    # insert the recipes into the treeview
    for recipe in default_recipes:
        recipesList.insert("", "end", values=(recipe["title"], recipe["category"], recipe["views"], recipe["createdAt"]))

    recipesList.place(x=50, y=100)

    # add scrollbar to the treeview
    scrollbar = ttk.Scrollbar(canvasRecipesCatalog, orient="vertical", command=recipesList.yview)
    scrollbar.place(x=660, y=100, height=430)

    recipesList.configure(yscrollcommand=scrollbar.set)

    # on click event to search for recipes
    btnSearch.bind("<Button-1>", lambda event: searchByTitle(inputSearch, recipesList, default_recipes))
    btnSearchIngredient.bind("<Button-1>", lambda event: searchByIngredient(inptutSearchIngredient, recipesList, default_recipes))


    RecipesCatalogWindow.protocol("WM_DELETE_WINDOW", lambda: [
                           RecipesCatalogWindow.destroy(), RecipesCategoryWindow.deiconify()])

    RecipesCatalogWindow.mainloop()


def searchByTitle(recipe, recipesList, default_recipes):

    recipesList.delete(*recipesList.get_children())

    searchVal = recipe.get()

    if (searchVal == ""):
        for recipe in default_recipes:
              recipesList.insert("", "end", values=(recipe["title"], recipe["category"], recipe["views"], recipe["createdAt"]))
    else:
        for recipe in default_recipes:
            if (searchVal.lower() in recipe["title"].lower()):
              recipesList.insert("", "end", values=(recipe["title"], recipe["category"], recipe["views"], recipe["createdAt"]))

def searchByIngredient(recipe, recipesList, default_recipes):

    recipesList.delete(*recipesList.get_children())

    searchVal = recipe.get()
    

    # if only contains digits
    if (searchVal.isdigit()):
        messagebox.showerror("Error", "Please enter a valid ingredient")
        return

    if (searchVal == ""):
        for recipe in default_recipes:
              recipesList.insert("", "end", values=(recipe["title"], recipe["category"], recipe["views"], recipe["createdAt"]))

    else:
        # join the recipes with the ingredients
        recipes = get_recipes_by_ingredient(default_recipes, searchVal)

        for recipe in recipes:
            recipesList.insert("", "end", values=(recipe["title"], recipe["category"], recipe["views"], recipe["createdAt"]))







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
    
    # treeview to display the recipes with columns title category views data
    recipesList = ttk.Treeview(canvasRecipesCatalog, columns=("title", "category", "views", "created date"), show="headings", height=20)
    
    recipesList.heading("title", text="Title")
    recipesList.heading("category", text="Category")
    recipesList.heading("views", text="Views")
    recipesList.heading("created date", text="Created Date")

    recipesList.column("title", width=150)
    recipesList.column("category", width=150, anchor="center")
    recipesList.column("views", width=150, anchor="center")
    recipesList.column("created date", width=150, anchor="center")
    
    # insert the recipes into the treeview
    for recipe in recipes:
        recipesList.insert("", "end", values=(recipe["title"], recipe["category"], recipe["views"], recipe["createdAt"]))

    recipesList.place(x=100, y=100)

    # # add scrollbar to the treeview
    # scrollbar = ttk.Scrollbar(canvasRecipesCatalog, orient="vertical", command=recipesList.yview)
    # scrollbar.place(x=1200, y=100, height=400)

    # recipesList.configure(yscrollcommand=scrollbar.set)


    RecipesCatalogWindow.protocol("WM_DELETE_WINDOW", lambda: [
                           RecipesCatalogWindow.destroy(), RecipesCategoryWindow.deiconify()])


    RecipesCatalogWindow.mainloop()
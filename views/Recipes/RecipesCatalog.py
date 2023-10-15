from tkinter import messagebox, Tk, Frame, TOP, X, NW, Canvas, Image, Button, Toplevel, ttk, Listbox
from PIL import ImageTk, Image
from classes.Navbar import NavbarWidget


def RecipesCatalogView(selectedCategory, user, RecipesCategoryWindow):

    RecipesCatalogWindow = Toplevel(RecipesCategoryWindow)

    print(selectedCategory)

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

    RecipesCatalogWindow.protocol("WM_DELETE_WINDOW", lambda: [
                           RecipesCatalogWindow.destroy(), RecipesCategoryWindow.deiconify()])


    RecipesCatalogWindow.mainloop()
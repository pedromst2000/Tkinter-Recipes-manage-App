from tkinter import messagebox, Tk, Frame, TOP, X, NW, Canvas, Image, Button, Toplevel, ttk, Listbox
from PIL import ImageTk, Image
from classes.Navbar import NavbarWidget
from models.Categories import get_categories
from views.Recipes.RecipesCatalog import RecipesCatalogView

def checkSelectedCategory(selectedCategory, user, RecipesCategoryWindow):

    if selectedCategory == "":
        messagebox.showerror(
            "Error", "You must select a category to see the recipes!")
    else:
        RecipesCatalogView(selectedCategory, user, RecipesCategoryWindow)
    

def RecipesCategoryView(user, Window):

    RecipesCategoryWindow = Toplevel(Window)

    # hide the main window
    Window.withdraw()

    categories = get_categories()
 
    RecipesCategoryWindow.title("CraftingCook - Recipes")

    RecipesCategoryWindow.geometry("1280x650")

    RecipesCategoryWindow.iconbitmap("assets/CraftingCook.ico")

    RecipesCategoryWindow.resizable(0, 0)

    navbar = NavbarWidget(
        RecipesCategoryWindow, 
        "assets/images/Home/notification.png", # notificationIcon
        "assets/images/Home/exit_app.png", # exitAppIcon
        user
    )
    navbar.create_widget()

    canvasRecipesCategory = Canvas(RecipesCategoryWindow, height=650, width=1280)
    canvasRecipesCategory.place(x=-2, y=100)

    image = Image.open("assets/images/Recipes/Recipes_Category_background.png")
    image = image.resize((1280, 650))

    image = ImageTk.PhotoImage(image)

    canvasRecipesCategory.create_image(0, 0, anchor=NW, image=image)

    # create text on canvas
    canvasRecipesCategory.create_text(640, 80, text="CraftingCook",
                           font=("Arial", 40, "bold"), fill="#E5B714")
    canvasRecipesCategory.create_text(640, 125, text="Choose a category", font=(
        "Arial", 20, "normal"), fill="#ffffff")

    # center a listbox 
    categoriesList = Listbox(RecipesCategoryWindow, width=50, height=15)
    # center the listbox
    categoriesList.place(x=640, y=420, anchor="center")

    # insert the categories in the listbox
    for category in categories:
        categoriesList.insert("end", category["category"])

    # add scrollbar
    scrollbar = ttk.Scrollbar(RecipesCategoryWindow, orient="vertical", command=categoriesList.yview)
    categoriesList.configure(yscrollcommand=scrollbar.set)
    # place the scrollbar on the right side
    scrollbar.place(x=800, y=420, anchor="center", height=240)

    btnSeeRecipes = Button(RecipesCategoryWindow, text="See Recipes", font=("Arial", 12, "bold"), bg="#B5960E", fg="white",  cursor="hand2", width=15, height=2, activebackground="#D1A711", activeforeground="#ffffff", bd=0)
    btnSeeRecipes.place(x=640, y=540, anchor="center")

    btnSeeRecipes.bind("<Button-1>", lambda event: [
        checkSelectedCategory(categoriesList.get("anchor"), user, RecipesCategoryWindow)
    ])

    # open the main window when the RecipesCategory window is closed
    RecipesCategoryWindow.protocol("WM_DELETE_WINDOW", lambda: [
                           RecipesCategoryWindow.destroy(), Window.deiconify()])
   
    RecipesCategoryWindow.mainloop()



from tkinter import messagebox, Tk, Frame, TOP, X, NW, Canvas, Image, Button, Toplevel
from PIL import ImageTk, Image
from classes.Navbar import NavbarWidget
from models.Categories import get_categories


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
    
    # render the buttons with the categories dynamically
    for i in range(len(categories)):
            buttonCategory = Button(canvasRecipesCategory, text=categories[i]["name"], font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                            cursor="hand2", width=10, height=2, activebackground="#D1A711", activeforeground="#ffffff", bd=0, compound=TOP, padx=15, pady=15)
            # Placing the button using the grid manager
            row = i // 3  # Calculate the row
            col = i % 3   # Calculate the column
            buttonCategory.grid(row=row, column=col)


    # open the main window when the RecipesCategory window is closed
    RecipesCategoryWindow.protocol("WM_DELETE_WINDOW", lambda: [
                           RecipesCategoryWindow.destroy(), Window.deiconify()])
   
    RecipesCategoryWindow.mainloop()



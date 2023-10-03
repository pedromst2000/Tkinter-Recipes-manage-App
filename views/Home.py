from tkinter import messagebox, Tk, Frame, TOP, X, NW, Canvas, Image, Button
from PIL import ImageTk, Image
from models.Users import checkLoggedUserRole, checkLoggedUserIsBlocked
from classes.Navbar import NavbarWidget


def HomeView(user, isLogged, isRegister):
    Window = Tk()

    Window.title("CraftingCook")
    Window.geometry("1280x650")

    Window.iconbitmap("assets/CraftingCook.ico")

    Window.resizable(0, 0)

    navbar = NavbarWidget(
        Window, 
        user["avatar"], # avatarUser 
        "assets/images/Home/notification.png", # notificationIcon
        "assets/images/Home/exit_app.png", # exitAppIcon
        user
    )
    navbar.create_widget()

    canvasHome = Canvas(Window, height=650, width=1280)
    canvasHome.place(x=-2, y=100)

    image = Image.open("assets/images/Home/home_image_V2.png")
    image = image.resize((1280, 650))

    image = ImageTk.PhotoImage(image)

    canvasHome.create_image(0, 0, anchor=NW, image=image)

    # create text on canvas
    canvasHome.create_text(640, 80, text="CraftingCook",
                           font=("Arial", 40, "bold"), fill="#E5B714")
    canvasHome.create_text(640, 125, text="Your Kitchen best friend", font=(
        "Arial", 20, "normal"), fill="#ffffff")


    # rendering the menu view conditionally
    if((isLogged == True and isRegister == False) or (isLogged == True and isRegister == True)) :
       
        if(checkLoggedUserRole(user["email"]) == "admin"):
            manageIcon = Image.open("assets/images/Home/manage_icon.png")

            manageIcon = manageIcon.resize((80, 80))

            manageIcon = ImageTk.PhotoImage(manageIcon)

            buttonManage = Button(canvasHome, text="Manage", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                          cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=manageIcon, compound=TOP, padx=15, pady=15)
            buttonManage.place(x=160, y=250)

            settingsIcon = Image.open("assets/images/Home/settings_icon.png")

            settingsIcon = settingsIcon.resize((80, 80))

            settingsIcon = ImageTk.PhotoImage(settingsIcon)

            buttonSettings = Button(canvasHome, text="Settings", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                            cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=settingsIcon, compound=TOP, padx=15, pady=15)

            buttonSettings.place(x=360, y=250)

            recipesIcon = Image.open("assets/images/Home/recipes_icon.png")

            recipesIcon = recipesIcon.resize((80, 80))

            recipesIcon = ImageTk.PhotoImage(recipesIcon)

            buttonRecipes = Button(canvasHome, text="Recipes", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                           cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=recipesIcon, compound=TOP, padx=15, pady=15)

            buttonRecipes.place(x=560, y=250)

            dashboardIcon = Image.open("assets/images/Home/dashboard_icon.png")

            dashboardIcon = dashboardIcon.resize((80, 80))

            dashboardIcon = ImageTk.PhotoImage(dashboardIcon)

            buttonDashboard = Button(canvasHome, text="Dashboard", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=dashboardIcon, compound=TOP, padx=15, pady=15)

            buttonDashboard.place(x=760, y=250)

            favoritesIcon = Image.open("assets/images/Home/favorites_icon.png")

            favoritesIcon = favoritesIcon.resize((80, 80))

            favoritesIcon = ImageTk.PhotoImage(favoritesIcon)

            buttonFavorites = Button(canvasHome, text="Favorites", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=favoritesIcon, compound=TOP, padx=15, pady=15)

            buttonFavorites.place(x=960, y=250)

        elif(checkLoggedUserRole(user["email"]) == "regular"):
            
            favoritesIcon = Image.open("assets/images/Home/favorites_icon.png")

            favoritesIcon = favoritesIcon.resize((100, 100))

            favoritesIcon = ImageTk.PhotoImage(favoritesIcon)

            buttonFavorites = Button(canvasHome, text="Favorites", font=("Arial", 13, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=favoritesIcon, compound=TOP, padx=25, pady=25)

            buttonFavorites.place(x=250, y=250)

            recipesIcon = Image.open("assets/images/Home/recipes_icon.png")

            recipesIcon = recipesIcon.resize((100, 100))

            recipesIcon = ImageTk.PhotoImage(recipesIcon)

            buttonRecipes = Button(canvasHome, text="Recipes", font=("Arial", 13, "bold"), bg="#B5960E", fg="white",
                           cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=recipesIcon, compound=TOP, padx=25, pady=25)

            buttonRecipes.place(x=560, y=250)

            dashboardIcon = Image.open("assets/images/Home/dashboard_icon.png")

            dashboardIcon = dashboardIcon.resize((100, 100))

            dashboardIcon = ImageTk.PhotoImage(dashboardIcon)

            buttonDashboard = Button(canvasHome, text="Dashboard", font=("Arial", 13, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=dashboardIcon, compound=TOP, padx=25, pady=25)

            buttonDashboard.place(x=860, y=250)

    Window.mainloop()
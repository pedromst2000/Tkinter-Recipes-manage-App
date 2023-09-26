import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from models.Users import checkLoggedUserRole, checkLoggedUserIsBlocked


def HomeView(user, isLogged, isRegister):

    if (isLogged == True and isRegister == False):
        if (checkLoggedUserRole(user["email"]) == "admin"):
            adminUserHomeView(user)

        if (checkLoggedUserRole(user["email"]) == "regular" and checkLoggedUserIsBlocked(user["email"]) == True):
            blockedUserHomeView(user)

        elif (checkLoggedUserRole(user["email"]) == "regular"):
            regularUserHomeView(user)

    elif (isLogged == True and isRegister == True):
        regularUserHomeView(user)


def adminUserHomeView(user):
    Window = Tk()

    Window.title("CraftingCook")
    Window.geometry("1280x800")

    Window.iconbitmap("assets/CraftingCook.ico")

    Window.resizable(0, 0)

    # navbar
    navbar = Frame(Window, bg="#E5B714", height=100)
    navbar.pack(side=TOP, fill=X)

    canvasAvatar = Canvas(navbar, height=70, width=70,
                          highlightthickness=0, cursor="hand2")
    canvasAvatar.place(x=20, y=15)

    # avatar
    avatar = Image.open(user["avatar"])

    avatar = avatar.resize((70, 70))

    avatar = ImageTk.PhotoImage(avatar)

    canvasAvatar.create_image(0, 0, anchor=NW, image=avatar)

    canvasNotification = Canvas(navbar, height=50, width=50, highlightthickness=0,
                                bg="#E5B714", cursor="hand2")
    canvasNotification.place(x=120, y=25)

    # notification
    notification = Image.open("assets/images/Home/notification.png")

    notification = notification.resize((50, 50))

    notification = ImageTk.PhotoImage(notification)

    canvasNotification.create_image(0, 0, anchor=NW, image=notification)

    canvasExitApp = Canvas(navbar, height=50, width=50,
                           highlightthickness=0, bg="#E5B714", cursor="hand2")
    canvasExitApp.place(x=1200, y=25)

    # exit app
    exitApp = Image.open("assets/images/Home/exit_app.png")

    exitApp = exitApp.resize((50, 50))

    exitApp = ImageTk.PhotoImage(exitApp)

    canvasExitApp.create_image(0, 0, anchor=NW, image=exitApp)

    # canvas
    canvasHome = Canvas(Window, height=760, width=1280)
    canvasHome.place(x=-2, y=100)

    image = Image.open("assets/images/Home/home_image_V2.png")
    image = image.resize((1280, 760))

    image = ImageTk.PhotoImage(image)

    canvasHome.create_image(0, 0, anchor=NW, image=image)

    # create text on canvas
    canvasHome.create_text(640, 80, text="CraftingCook",
                           font=("Arial", 40, "bold"), fill="#E5B714")
    canvasHome.create_text(640, 620, text="Your Kitchen best friend", font=(
        "Arial", 25, "normal"), fill="#ffffff")

    manageIcon = Image.open("assets/images/Home/Manage_icon.png")

    manageIcon = manageIcon.resize((80, 80))

    manageIcon = ImageTk.PhotoImage(manageIcon)

    buttonManage = Button(canvasHome, text="Manage", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                          cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=manageIcon, compound=TOP, padx=15, pady=15)
    buttonManage.place(x=160, y=250)

    settingsIcon = Image.open("assets/images/Home/Settings_icon.png")

    settingsIcon = settingsIcon.resize((80, 80))

    settingsIcon = ImageTk.PhotoImage(settingsIcon)

    buttonSettings = Button(canvasHome, text="Settings", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                            cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=settingsIcon, compound=TOP, padx=15, pady=15)

    buttonSettings.place(x=360, y=250)

    recipesIcon = Image.open("assets/images/Home/Recipes_icon.png")

    recipesIcon = recipesIcon.resize((80, 80))

    recipesIcon = ImageTk.PhotoImage(recipesIcon)

    buttonRecipes = Button(canvasHome, text="Recipes", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                           cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=recipesIcon, compound=TOP, padx=15, pady=15)

    buttonRecipes.place(x=560, y=250)

    dashboardIcon = Image.open("assets/images/Home/Dashboard_icon.png")

    dashboardIcon = dashboardIcon.resize((80, 80))

    dashboardIcon = ImageTk.PhotoImage(dashboardIcon)

    buttonDashboard = Button(canvasHome, text="Dashboard", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=dashboardIcon, compound=TOP, padx=15, pady=15)

    buttonDashboard.place(x=760, y=250)

    favoritesIcon = Image.open("assets/images/Home/Favorites_icon.png")

    favoritesIcon = favoritesIcon.resize((80, 80))

    favoritesIcon = ImageTk.PhotoImage(favoritesIcon)

    buttonFavorites = Button(canvasHome, text="Favorites", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=favoritesIcon, compound=TOP, padx=15, pady=15)

    buttonFavorites.place(x=960, y=250)

    Window.mainloop()


def blockedUserHomeView(user):
    Window = Tk()

    Window.title("CraftingCook")
    Window.geometry("1280x800")

    Window.iconbitmap("assets/CraftingCook.ico")

    Window.resizable(0, 0)

    # navbar
    navbar = Frame(Window, bg="#E5B714", height=100)
    navbar.pack(side=TOP, fill=X)

    # round canvas for the avatar
    canvasAvatar = Canvas(navbar, height=70, width=70, highlightthickness=0)
    canvasAvatar.place(x=20, y=15)

    # avatar
    avatar = Image.open(user["avatar"])

    avatar = avatar.resize((70, 70))

    avatar = ImageTk.PhotoImage(avatar)

    canvasAvatar.create_image(0, 0, anchor=NW, image=avatar)

    Window.mainloop()


def regularUserHomeView(user):
    Window = Tk()

    Window.title("CraftingCook")
    Window.geometry("1280x800")

    Window.iconbitmap("assets/CraftingCook.ico")

    Window.resizable(0, 0)

    # navbar
    navbar = Frame(Window, bg="#E5B714", height=100)
    navbar.pack(side=TOP, fill=X)

    # round canvas for the avatar
    canvasAvatar = Canvas(navbar, height=70, width=70, highlightthickness=0)
    canvasAvatar.place(x=20, y=15)

    # avatar
    avatar = Image.open(user["avatar"])

    avatar = avatar.resize((70, 70))

    avatar = ImageTk.PhotoImage(avatar)

    canvasAvatar.create_image(0, 0, anchor=NW, image=avatar)

    Window.mainloop()

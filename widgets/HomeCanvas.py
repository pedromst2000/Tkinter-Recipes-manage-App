from tkinter import TOP, NW, Canvas, Image, Button
from PIL import ImageTk, Image

class HomeCanvasWidget:
    def __init__(self, Window, user, manageIcon, settingsIcon, recipesIcon, dashboardIcon, favoritesIcon, HomeImage):
        self.Window = Window
        self.user = user
        self.manageIcon = manageIcon
        self.settingsIcon = settingsIcon
        self.recipesIcon = recipesIcon
        self.dashboardIcon = dashboardIcon
        self.favoritesIcon = favoritesIcon
        self.HomeImage = HomeImage

    # method to create the canvas widget
    def create_widget(self):
           # canvas
        canvasHome = Canvas(self.Window, height=650, width=1280)
        canvasHome.place(x=-2, y=100)

        image = Image.open(self.HomeImage)
        image = image.resize((1280, 650))

        self.image = ImageTk.PhotoImage(image)

        canvasHome.create_image(0, 0, anchor=NW, image=self.image)

    # create text on canvas
        canvasHome.create_text(640, 80, text="CraftingCook",
                           font=("Arial", 40, "bold"), fill="#E5B714")
        canvasHome.create_text(640, 125, text="Your Kitchen best friend", font=(
        "Arial", 20, "normal"), fill="#ffffff")

        if(self.user["role"] == "admin" ):
            manageIcon = Image.open(self.manageIcon)

            manageIcon = manageIcon.resize((80, 80))

            self.manageIcon = ImageTk.PhotoImage(manageIcon)

            buttonManage = Button(canvasHome, text="Manage", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                          cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.manageIcon, compound=TOP, padx=15, pady=15)
            buttonManage.place(x=160, y=250)

            settingsIcon = Image.open(self.settingsIcon)

            settingsIcon = settingsIcon.resize((80, 80))

            self.settingsIcon = ImageTk.PhotoImage(settingsIcon)

            buttonSettings = Button(canvasHome, text="Settings", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                            cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.settingsIcon, compound=TOP, padx=15, pady=15)

            buttonSettings.place(x=360, y=250)

            recipesIcon = Image.open(self.recipesIcon)

            recipesIcon = recipesIcon.resize((80, 80))

            self.recipesIcon = ImageTk.PhotoImage(recipesIcon)

            buttonRecipes = Button(canvasHome, text="Recipes", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                           cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.recipesIcon, compound=TOP, padx=15, pady=15)

            buttonRecipes.place(x=560, y=250)

            dashboardIcon = Image.open(self.dashboardIcon)

            dashboardIcon = dashboardIcon.resize((80, 80))

            self.dashboardIcon = ImageTk.PhotoImage(dashboardIcon)

            buttonDashboard = Button(canvasHome, text="Dashboard", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.dashboardIcon, compound=TOP, padx=15, pady=15)

            buttonDashboard.place(x=760, y=250)

            favoritesIcon = Image.open(self.favoritesIcon)

            favoritesIcon = favoritesIcon.resize((80, 80))

            self.favoritesIcon = ImageTk.PhotoImage(favoritesIcon)

            buttonFavorites = Button(canvasHome, text="Favorites", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.favoritesIcon, compound=TOP, padx=15, pady=15)

            buttonFavorites.place(x=960, y=250)

        else:
                
            canvasHome = Canvas(self.Window, height=650, width=1280)
            canvasHome.place(x=-2, y=100)

            image = Image.open(self.HomeImage)
            image = image.resize((1280, 650))

            image = ImageTk.PhotoImage(image)

            canvasHome.create_image(0, 0, anchor=NW, image=self.image)

            # create text on canvas
            canvasHome.create_text(640, 80, text="CraftingCook",
                           font=("Arial", 40, "bold"), fill="#E5B714")
            canvasHome.create_text(640, 125, text="Your Kitchen best friend", font=(
            "Arial", 20, "normal"), fill="#ffffff")

            favoritesIcon = Image.open(self.favoritesIcon)

            favoritesIcon = favoritesIcon.resize((100, 100))

            self.favoritesIcon = ImageTk.PhotoImage(favoritesIcon)

            buttonFavorites = Button(canvasHome, text="Favorites", font=("Arial", 13, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.favoritesIcon, compound=TOP, padx=25, pady=25)

            buttonFavorites.place(x=250, y=250)

            recipesIcon = Image.open(self.recipesIcon)

            recipesIcon = recipesIcon.resize((100, 100))

            self.recipesIcon = ImageTk.PhotoImage(recipesIcon)

            buttonRecipes = Button(canvasHome, text="Recipes", font=("Arial", 13, "bold"), bg="#B5960E", fg="white",
                           cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.recipesIcon, compound=TOP, padx=25, pady=25)

            buttonRecipes.place(x=560, y=250)

            dashboardIcon = Image.open(self.dashboardIcon)

            dashboardIcon = dashboardIcon.resize((100, 100))

            self.dashboardIcon = ImageTk.PhotoImage(dashboardIcon)

            buttonDashboard = Button(canvasHome, text="Dashboard", font=("Arial", 13, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.dashboardIcon, compound=TOP, padx=25, pady=25)

            buttonDashboard.place(x=860, y=250)
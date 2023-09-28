class HomeCanvasWidget:
    def __init__(self, Canvas, Window, Image, ImageTk, image, NW, user, Button, TOP, manageIcon, settingsIcon, recipesIcon, dashboardIcon, favoritesIcon, HomeImage):
        self.Canvas = Canvas
        self.Window = Window
        self.Image = Image
        self.ImageTk = ImageTk
        self.image = image
        self.NW = NW
        self.user = user
        self.Button = Button
        self.TOP = TOP
        self.manageIcon = manageIcon
        self.settingsIcon = settingsIcon
        self.recipesIcon = recipesIcon
        self.dashboardIcon = dashboardIcon
        self.favoritesIcon = favoritesIcon
        self.HomeImage = HomeImage

    # method to create the canvas widget
    def create_widget(self):
           # canvas
        canvasHome = self.Canvas(self.Window, height=650, width=1280)
        canvasHome.place(x=-2, y=100)

        image = self.Image.open(self.HomeImage)
        image = image.resize((1280, 650))

        self.image = self.ImageTk.PhotoImage(image)

        canvasHome.create_image(0, 0, anchor=self.NW, image=self.image)

    # create text on canvas
        canvasHome.create_text(640, 80, text="CraftingCook",
                           font=("Arial", 40, "bold"), fill="#E5B714")
        canvasHome.create_text(640, 125, text="Your Kitchen best friend", font=(
        "Arial", 20, "normal"), fill="#ffffff")

        if(self.user["role"] == "admin" ):
            manageIcon = self.Image.open(self.manageIcon)

            manageIcon = manageIcon.resize((80, 80))

            self.manageIcon = self.ImageTk.PhotoImage(manageIcon)

            buttonManage = self.Button(canvasHome, text="Manage", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                          cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.manageIcon, compound=self.TOP, padx=15, pady=15)
            buttonManage.place(x=160, y=250)

            settingsIcon = self.Image.open(self.settingsIcon)

            settingsIcon = settingsIcon.resize((80, 80))

            self.settingsIcon = self.ImageTk.PhotoImage(settingsIcon)

            buttonSettings = self.Button(canvasHome, text="Settings", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                            cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.settingsIcon, compound=self.TOP, padx=15, pady=15)

            buttonSettings.place(x=360, y=250)

            recipesIcon = self.Image.open(self.recipesIcon)

            recipesIcon = recipesIcon.resize((80, 80))

            self.recipesIcon = self.ImageTk.PhotoImage(recipesIcon)

            buttonRecipes = self.Button(canvasHome, text="Recipes", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                           cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.recipesIcon, compound=self.TOP, padx=15, pady=15)

            buttonRecipes.place(x=560, y=250)

            dashboardIcon = self.Image.open(self.dashboardIcon)

            dashboardIcon = dashboardIcon.resize((80, 80))

            self.dashboardIcon = self.ImageTk.PhotoImage(dashboardIcon)

            buttonDashboard = self.Button(canvasHome, text="Dashboard", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.dashboardIcon, compound=self.TOP, padx=15, pady=15)

            buttonDashboard.place(x=760, y=250)

            favoritesIcon = self.Image.open(self.favoritesIcon)

            favoritesIcon = favoritesIcon.resize((80, 80))

            self.favoritesIcon = self.ImageTk.PhotoImage(favoritesIcon)

            buttonFavorites = self.Button(canvasHome, text="Favorites", font=("Arial", 10, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.favoritesIcon, compound=self.TOP, padx=15, pady=15)

            buttonFavorites.place(x=960, y=250)

        else:
                
            canvasHome = self.Canvas(self.Window, height=650, width=1280)
            canvasHome.place(x=-2, y=100)

            image = self.Image.open(self.HomeImage)
            image = image.resize((1280, 650))

            image = self.ImageTk.PhotoImage(image)

            canvasHome.create_image(0, 0, anchor=self.NW, image=self.image)

            # create text on canvas
            canvasHome.create_text(640, 80, text="CraftingCook",
                           font=("Arial", 40, "bold"), fill="#E5B714")
            canvasHome.create_text(640, 125, text="Your Kitchen best friend", font=(
            "Arial", 20, "normal"), fill="#ffffff")

            favoritesIcon = self.Image.open(self.favoritesIcon)

            favoritesIcon = favoritesIcon.resize((100, 100))

            self.favoritesIcon = self.ImageTk.PhotoImage(favoritesIcon)

            buttonFavorites = self.Button(canvasHome, text="Favorites", font=("Arial", 13, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.favoritesIcon, compound=self.TOP, padx=25, pady=25)

            buttonFavorites.place(x=250, y=250)

            recipesIcon = self.Image.open(self.recipesIcon)

            recipesIcon = recipesIcon.resize((100, 100))

            self.recipesIcon = self.ImageTk.PhotoImage(recipesIcon)

            buttonRecipes = self.Button(canvasHome, text="Recipes", font=("Arial", 13, "bold"), bg="#B5960E", fg="white",
                           cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.recipesIcon, compound=self.TOP, padx=25, pady=25)

            buttonRecipes.place(x=560, y=250)

            dashboardIcon = self.Image.open(self.dashboardIcon)

            dashboardIcon = dashboardIcon.resize((100, 100))

            self.dashboardIcon = self.ImageTk.PhotoImage(dashboardIcon)

            buttonDashboard = self.Button(canvasHome, text="Dashboard", font=("Arial", 13, "bold"), bg="#B5960E", fg="white",
                             cursor="hand2", width=100, height=120, activebackground="#D1A711", activeforeground="#ffffff", bd=0, image=self.dashboardIcon, compound=self.TOP, padx=25, pady=25)

            buttonDashboard.place(x=860, y=250)
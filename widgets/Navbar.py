class NavbarWidget:
    def __init__(self, Frame, Window, TOP, X, NW, Canvas, Image, ImageTk, avatarUser, notificationIcon, exitAppIcon):
        self.Frame = Frame
        self.Window = Window
        self.TOP = TOP
        self.X = X
        self.NW = NW
        self.Canvas = Canvas
        self.Image = Image
        self.ImageTk = ImageTk
        self.avatarUser = avatarUser
        self.notificationIcon = notificationIcon
        self.exitAppIcon = exitAppIcon

    # method to create the navbar widget
    def create_widget(self):
        navbar = self.Frame(self.Window, bg="#E5B714", height=100)
        navbar.pack(side=self.TOP, fill=self.X)

        canvasAvatar = self.Canvas(navbar, height=70, width=70,
                                   highlightthickness=0, cursor="hand2")
        canvasAvatar.place(x=20, y=15)

        avatar = self.Image.open(self.avatarUser)
        avatar = avatar.resize((70, 70))
        self.avatar = self.ImageTk.PhotoImage(avatar)  # Store as an instance variable

        canvasAvatar.create_image(0, 0, anchor=self.NW, image=self.avatar)

        canvasNotification = self.Canvas(navbar, height=50, width=50, highlightthickness=0,
                                         bg="#E5B714", cursor="hand2")
        canvasNotification.place(x=120, y=25)

        notification = self.Image.open(self.notificationIcon)
        notification = notification.resize((50, 50))
        self.notification = self.ImageTk.PhotoImage(notification)  # Store as an instance variable

        canvasNotification.create_image(0, 0, anchor=self.NW, image=self.notification)

        canvasExitApp = self.Canvas(navbar, height=50, width=50,
                                    highlightthickness=0, bg="#E5B714", cursor="hand2")
        canvasExitApp.place(x=1200, y=25)

        exitApp = self.Image.open(self.exitAppIcon)
        exitApp = exitApp.resize((50, 50))
        self.exitApp = self.ImageTk.PhotoImage(exitApp)  # Store as an instance variable

        canvasExitApp.create_image(0, 0, anchor=self.NW, image=self.exitApp)

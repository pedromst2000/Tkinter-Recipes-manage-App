from widgets.Avatar import Avatar
from tkinter import Frame, TOP, X, NW, Canvas, Image
from PIL import ImageTk, Image

class NavbarWidget:
    def __init__(self, Window, avatarUser, notificationIcon, exitAppIcon, user):
        self.Window = Window
        self.avatarUser = avatarUser
        self.notificationIcon = notificationIcon
        self.exitAppIcon = exitAppIcon
        self.user = user

    # method to create the navbar widget
    def create_widget(self):
        navbar = Frame(self.Window, bg="#E5B714", height=100)
        navbar.pack(side=TOP, fill=X)

        # avatar
        avatar = Avatar(
            self.avatarUser, # avatar image
            "hand2", # cursor
            70, # height
            70, # width
            20, # x
            15, # y
            70, # radius
            70, # borderwidth
            0, # highlightthickness
            0, # bd
            self.Window,
            self.user
        )

        avatar.create_widget()

        # bind - onCLick will call the ProfileView function with the window as parameter to be able to destroy it after the successful authentication

        canvasNotification = Canvas(navbar, height=50, width=50, highlightthickness=0,
                                         bg="#E5B714", cursor="hand2")
        canvasNotification.place(x=120, y=25)

        notification = Image.open(self.notificationIcon)
        notification = notification.resize((50, 50))
        self.notification = ImageTk.PhotoImage(notification)  # Store as an instance variable

        canvasNotification.create_image(0, 0, anchor=NW, image=self.notification)

        canvasExitApp = Canvas(navbar, height=50, width=50,
                                    highlightthickness=0, bg="#E5B714", cursor="hand2")
        canvasExitApp.place(x=1200, y=25)

        exitApp = Image.open(self.exitAppIcon)
        exitApp = exitApp.resize((50, 50))
        self.exitApp = ImageTk.PhotoImage(exitApp)  # Store as an instance variable

        canvasExitApp.create_image(0, 0, anchor=NW, image=self.exitApp)

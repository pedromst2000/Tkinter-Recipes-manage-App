from tkinter import Frame, TOP, X, NW, Canvas, Image
from PIL import ImageTk, Image
from views.Profile import ProfileView
from models.Users import get_user

class NavbarWidget:
    def __init__(self, Window, notificationIcon, exitAppIcon, user):
        self.Window = Window
        self.notificationIcon = notificationIcon
        self.exitAppIcon = exitAppIcon
        self.user = user

    # method to create the navbar widget
    def create_widget(self):
        navbar = Frame(self.Window, bg="#E5B714", height=100)
        navbar.pack(side=TOP, fill=X)

        canvasAvatar = Canvas(navbar, height=70, width=70, highlightthickness=0, bg="#E5B714", cursor="hand2")

        canvasAvatar.place(x=20, y=15)

        avatar = Image.open(get_user(self.user["email"])["avatar"])

        avatar = avatar.resize((70, 70))

        self.avatar = ImageTk.PhotoImage(avatar)  # Store as an instance variable

        canvasAvatar.create_image(0, 0, anchor=NW, image=self.avatar)


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
        
        canvasAvatar.bind("<Button-1>", lambda event: ProfileView(self.Window, self.user))

        canvasExitApp.create_image(0, 0, anchor=NW, image=self.exitApp)

    
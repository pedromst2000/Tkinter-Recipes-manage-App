from views.Profile.Profile import ProfileView
from tkinter import Canvas, NW, Image
from PIL import ImageTk, Image

class Avatar:
    def __init__(self, avatarUser, cursor, width, height, placeX, placeY, resizeX, resizeY, canvasX, canvasY, Window, user):
        self.avatarUser = avatarUser
        self.cursor = cursor
        self.width = width
        self.height = height
        self.placeX = placeX
        self.placeY = placeY
        self.resizeX = resizeX
        self.resizeY = resizeY
        self.canvasX = canvasX
        self.canvasY = canvasY
        self.Window = Window
        self.user = user

    def create_widget(self):
        canvasAvatar = Canvas(self.Window, height=self.height, width=self.width,
                               highlightthickness=0, cursor=self.cursor)
        canvasAvatar.place(x=self.placeX, y=self.placeY)

        avatar = Image.open(self.avatarUser)
        avatar = avatar.resize((self.resizeX, self.resizeY))
        self.avatar = ImageTk.PhotoImage(avatar)  # Store as an instance variable

        canvasAvatar.create_image(self.canvasX, self.canvasY, anchor=NW, image=self.avatar)


    # checking if the avatar is in the navbar
        if (self.placeX == 20 and self.placeY == 15): # if the avatar is in the navbar (checking the coordinates)
            # bind - onCLick will call the ProfileView function
            canvasAvatar.bind("<Button-1>", lambda event: ProfileView(self.Window, self.user))
        else:
            return None # if the avatar is not in the navbar, return None
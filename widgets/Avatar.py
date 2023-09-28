class Avatar:
    def __init__(self, Canvas, Image, ImageTk, avatarUser, NW):
        self.Canvas = Canvas
        self.Image = Image
        self.ImageTk = ImageTk
        self.avatarUser = avatarUser
        self.NW = NW


    # method to create the avatar widget
    def create_widget(self):
        canvasAvatar = self.Canvas(self, height=70, width=70,
                                   highlightthickness=0, cursor="")
        canvasAvatar.place(x=20, y=15)

        avatar = self.Image.open(self.avatarUser)
        avatar = avatar.resize((70, 70))
        self.avatar = self.ImageTk.PhotoImage(avatar)  # Store as an instance variable

        canvasAvatar.create_image(0, 0, anchor=self.NW, image=self.avatar)
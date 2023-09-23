from tkinter import *
from PIL import ImageTk, Image
from views.Authentication import loginView, registerView

Window = Tk()

Window.title("CraftingCook")
Window.geometry("1280x800")

# to insert the icon on the window
Window.iconbitmap("assets/CraftingCook.ico")

# remove the maximize button
Window.resizable(0, 0)

# navbar
navbar = Frame(Window, bg="#E5B714", height=100)
navbar.pack(side=TOP, fill=X)

# btn Login
btnLogin = Button(navbar, text="Login", font=("Arial", 12, "bold"), bg="#B5960E", fg="white",  cursor="hand2", width=10, height=2, activebackground="#D1A711", activeforeground="#ffffff", bd=0)
btnLogin.place(x=1000, y=25)

# btn Register
btnRegister = Button(navbar, text="Register", font=("Arial", 12, "bold"), bg="#B5960E", fg="white",  cursor="hand2", width=10, height=2, activebackground="#D1A711", activeforeground="#ffffff", bd=0)
btnRegister.place(x=1140, y=25)

# canvas
canvasMain = Canvas(Window, bg="grey", height=760, width=1280)
canvasMain.place(x=-2, y=100)

# # image
image = Image.open("assets/images/home_image.png")
image = image.resize((1280, 760))

image = ImageTk.PhotoImage(image)

canvasMain.create_image(0, 0, anchor=NW, image=image)

# bind - onCLick will call the loginView or the registerView function with the window as parameter to be able to destroy it after the sucessfull authentication
btnLogin.bind("<Button-1>", lambda event: loginView(Window))
btnRegister.bind("<Button-1>", lambda event: registerView(Window))

Window.mainloop()
import tkinter as tk
from tkinter import messagebox, Canvas, NW, TOP, X, Button, Frame
from PIL import ImageTk, Image
from models.Authenticate import login
from utils import checkEmail
from views.Home import HomeView

isLogged = False


def loginView():
    # open the window
    loginWindow = tk.Toplevel()
    loginWindow.title("Login")
    loginWindow.iconbitmap("assets/CraftingCook.ico")
    loginWindow.geometry("560x540")
    loginWindow.resizable(0, 0)
    loginWindow.config(bg="#806B14")

    # # canvas
    canvasLogin = Canvas(loginWindow,  height=160,
                         width=180, highlightthickness=0)
    # center
    canvasLogin.place(x=200, y=50)

    login_image = Image.open("assets/images/login_image.png")
    login_image = login_image.resize((180, 160))

    canvasLogin.image = ImageTk.PhotoImage(login_image)

    canvasLogin.create_image(0, 0, anchor=NW, image=canvasLogin.image)

    labelEmail = tk.Label(loginWindow, text="Email", font=(
        "Arial", 12, "bold"), bg="#806B14", fg="white")
    labelEmail.place(x=120, y=250)

    inputEmail = tk.Entry(loginWindow, width=38, font=(
        "Arial", 11, "bold"), bg="white", fg="#806B14", bd=0)
    inputEmail.place(x=120, y=280)

    labelPassword = tk.Label(loginWindow, text="Password", font=(
        "Arial", 12, "bold"), bg="#806B14", fg="white")
    labelPassword.place(x=120, y=320)

    inputPassword = tk.Entry(loginWindow, width=38, font=(
        "Arial", 11, "bold"), bg="white", fg="#806B14", bd=0, show="*")
    inputPassword.place(x=120, y=350)

    labelInfo = tk.Label(loginWindow, text="Don't have an account? Sign up", font=(
        "Arial", 12), bg="#806B14", fg="white", cursor="hand2")
    labelInfo.place(x=155, y=400)

    # on mouse hover in and out underline the text
    def on_enter(e):
        labelInfo.config(font=("Arial", 12, "underline"))

    def on_leave(e):
        labelInfo.config(font=("Arial", 12))

    labelInfo.bind("<Enter>", on_enter)
    labelInfo.bind("<Leave>", on_leave)

    btnLogin = Button(loginWindow, text="Login", font=(
        "Arial", 12, "bold"), bg="#B5960E", fg="white",  cursor="hand2", width=10, height=2)
    # center
    btnLogin.place(x=210, y=450)

    btnLogin.bind("<Button-1>", lambda event: checkLogin(
        inputEmail.get(), inputPassword.get(), loginWindow))

    loginWindow.grab_set()


def checkLogin(email, password, loginWindow):

    global isLogged, isAdmin, isBlocked

    if (email == "" or password == ""):
        return messagebox.showerror("Error", "Email and password are required")

    elif (checkEmail(email) == False):
        return messagebox.showerror("Error", "Invalid email")

    # check if the user exists
    user = login(email, password)

    if (user == None):
        messagebox.showerror("Error", "Invalid email or password")

    elif (user != None):
        messagebox.showinfo(
            "Success", f"Welcome back Chief {user['username']}")

        isLogged = True

        loginWindow.destroy()

        HomeView(user, isLogged)


def registerView():

    print("register View")



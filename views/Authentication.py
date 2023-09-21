import tkinter as tk
from tkinter import messagebox, Canvas, NW, TOP, X, Button, Frame
from PIL import ImageTk, Image
from models.Authenticate import login
from utils import checkEmail
from views.Home import HomeView

# global variable
isLogged = False  # this variable will be used to check if the user is logged or not
# this variable will be used to check if the password is visible or not
isPasswordVisible = False


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

    login_image = Image.open("assets/images/auth_image.png")
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

    canvasManagePassword = Canvas(loginWindow,  height=20,
                                  width=80, highlightthickness=0, cursor="hand2", bg="white")


    def managePassword():

        global isPasswordVisible

        if(inputPassword.get() != "" or isPasswordVisible == False):
            
            eye = Image.open("assets/images/hidden_password.png")

            eye = eye.resize((20, 20))

            canvasManagePassword.image = ImageTk.PhotoImage(eye)

            canvasManagePassword.create_image(
                0, 0, anchor=NW, image=canvasManagePassword.image)
            
            canvasManagePassword.place(x=450, y=350)
        
        elif(inputPassword.get() != "" or isPasswordVisible == True):
            
            eye = Image.open("assets/images/visible_password.png")

            eye = eye.resize((20, 20))

            canvasManagePassword.image = ImageTk.PhotoImage(eye)

            canvasManagePassword.create_image(
                0, 0, anchor=NW, image=canvasManagePassword.image)
            
            canvasManagePassword.place(x=450, y=350)

        else:
            canvasManagePassword.place_forget()


    inputPassword.bind("<KeyRelease>", lambda event: managePassword())



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

    global isLogged

    if (email == "" or password == ""):
        return messagebox.showerror("Error", "Email and password are required")

    elif (checkEmail(email) == False):
        return messagebox.showerror("Error", "Invalid email")

    # check if the user exists
    user = login(email, password)

    if (user == None):
        messagebox.showerror("Error", "Invalid Credentials")

    elif (user != None):
        messagebox.showinfo(
            "Success", f"Welcome back Chief {user['username']}")

        isLogged = True

        loginWindow.destroy()

        # the Home view will be different depending on the state of the logged user (role, isBlocked)
        HomeView(user, isLogged)


def registerView():
    registerWindow = tk.Toplevel()
    registerWindow.title("Register")
    registerWindow.iconbitmap("assets/CraftingCook.ico")
    registerWindow.geometry("560x660")
    registerWindow.resizable(0, 0)
    registerWindow.config(bg="#806B14")

    registerWindow.grab_set()  # to block the main window

    # # canvas
    canvasRegister = Canvas(registerWindow,  height=160,
                            width=180, highlightthickness=0)
    # center
    canvasRegister.place(x=200, y=50)

    register_image = Image.open("assets/images/auth_image.png")
    register_image = register_image.resize((180, 160))

    canvasRegister.image = ImageTk.PhotoImage(register_image)

    canvasRegister.create_image(0, 0, anchor=NW, image=canvasRegister.image)

    labelUsername = tk.Label(registerWindow, text="Username", font=(
        "Arial", 12, "bold"), bg="#806B14", fg="white")
    labelUsername.place(x=120, y=230)

    inputUsername = tk.Entry(registerWindow, width=38, font=(
        "Arial", 11, "bold"), bg="white", fg="#806B14", bd=0)
    inputUsername.place(x=120, y=260)

    labelEmail = tk.Label(registerWindow, text="Email", font=(
        "Arial", 12, "bold"), bg="#806B14", fg="white")
    labelEmail.place(x=120, y=300)

    inputEmail = tk.Entry(registerWindow, width=38, font=(
        "Arial", 11, "bold"), bg="white", fg="#806B14", bd=0)
    inputEmail.place(x=120, y=330)

    labelPassword = tk.Label(registerWindow, text="Password", font=(
        "Arial", 12, "bold"), bg="#806B14", fg="white")
    labelPassword.place(x=120, y=370)

    inputPassword = tk.Entry(registerWindow, width=38, font=(
        "Arial", 11, "bold"), bg="white", fg="#806B14", bd=0, show="*")
    inputPassword.place(x=120, y=400)

    labelConfirmPassword = tk.Label(registerWindow, text="Confirm Password", font=(
        "Arial", 12, "bold"), bg="#806B14", fg="white")
    labelConfirmPassword.place(x=120, y=440)

    inputConfirmPassword = tk.Entry(registerWindow, width=38, font=(
        "Arial", 11, "bold"), bg="white", fg="#806B14", bd=0, show="*")
    inputConfirmPassword.place(x=120, y=470)

    labelInfo = tk.Label(registerWindow, text="Already have an account? Sign In", font=(
        "Arial", 12), bg="#806B14", fg="white", cursor="hand2")
    labelInfo.place(x=140, y=525)

    # on mouse hover in and out underline the text
    def on_enter(e):
        labelInfo.config(font=("Arial", 12, "underline"))

    def on_leave(e):
        labelInfo.config(font=("Arial", 12))

    labelInfo.bind("<Enter>", on_enter)
    labelInfo.bind("<Leave>", on_leave)

    btnRegister = Button(registerWindow, text="Register", font=(
        "Arial", 12, "bold"), bg="#B5960E", fg="white",  cursor="hand2", width=10, height=2)
    # center
    btnRegister.place(x=210, y=570)

    # btnRegister.bind("<Button-1>", lambda event: checkLogin(
    #     inputEmail.get(), inputPassword.get(), registerWindow))




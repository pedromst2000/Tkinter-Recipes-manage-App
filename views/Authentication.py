import tkinter as tk
from tkinter import messagebox, Canvas, NW, TOP, X, Button, Frame
from PIL import ImageTk, Image
from models.Authenticate import login, register, checkRegisterUsername, checkRegisterEmail
from utils import checkEmail, togglePasswordVisibility, manageVisibility
from views.Home import HomeView

# global variable
isLogged = False  # this variable will be used to check if the user is logged or not
isRegister = False  # this variable will be used to check if the user is registering or not

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

    canvasManagePassword = Canvas(loginWindow,  height=26,
                                  width=40, highlightthickness=0, cursor="hand2")
    
    canvasManagePassword.config(highlightthickness=0, bd=0, bg="#806B14")

 
    # bind - when the user clicks (onClick) on the canvas, the function will be called
    canvasManagePassword.bind("<Button-1>", lambda event: togglePasswordVisibility(
        ImageTk, Image, canvasManagePassword, NW, inputPassword, 435, 348
    ))

    # bind - when the user releases the key (onKeyPress), the function will be called
    inputPassword.bind("<KeyRelease>", lambda event: manageVisibility(
        ImageTk, Image, canvasManagePassword, NW, inputPassword, 435, 348
    ))


    labelInfo = tk.Label(loginWindow, text="Don't have an account? Sign up", font=(
        "Arial", 12), bg="#806B14", fg="white", cursor="hand2")
    labelInfo.place(x=155, y=400)

    # on mouse hover in and out underline the text
    def on_enter(e):
        labelInfo.config(font=("Arial", 12, "underline"))

    def on_leave(e):
        labelInfo.config(font=("Arial", 12))

    # bind - when the user hovers the mouse on the label, the function will be called
    labelInfo.bind("<Enter>", on_enter)
    labelInfo.bind("<Leave>", on_leave) # when the user leaves the label, the function will be called

    labelInfo.bind("<Button-1>", lambda event: openSignUpLink(event, loginWindow))

    btnLogin = Button(loginWindow, text="Login", font=(
        "Arial", 12, "bold"), bg="#B5960E", fg="white",  cursor="hand2", width=10, height=2)
    # center
    btnLogin.place(x=210, y=450)

    # bind - when the user clicks (onClick) on the button, will trigger checkLogin function
    btnLogin.bind("<Button-1>", lambda event: checkLogin(
        inputEmail.get(), inputPassword.get(), loginWindow))

    loginWindow.grab_set() # to block the main window


def checkLogin(email, password, loginWindow):

    global isLogged, isRegister

    if (email == "" or password == ""):
        return messagebox.showerror("Error", "Email and password are required")

    elif (checkEmail(email) == False): # checking with the util function if the email is valid
        return messagebox.showerror("Error", "Invalid email")

    user = login(email, password) # this function returns the user if the email and password are correct, otherwise returns None

    if (user == None): # if the user doesn't exist
        messagebox.showerror("Error", "Invalid Credentials")

    elif (user != None): # if the user exists
        messagebox.showinfo(
            "Success", f"Welcome back Chief {user['username']}")

        isLogged = True
        isRegister = False

        loginWindow.destroy() # destroy the login window

        # the Home view will be different depending on the state of the logged user (role, isBlocked)
        HomeView(user, isLogged, isRegister)


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

    canvasManagePassword = Canvas(registerWindow,  height=26,
                                  width=40, highlightthickness=0, cursor="hand2")
    
    canvasManagePassword.config(highlightthickness=0, bd=0, bg="#806B14")
    
    canvasManagePassword.bind("<Button-1>", lambda event: togglePasswordVisibility(
        ImageTk, Image, canvasManagePassword, NW, inputPassword, 435, 398
    ))

    inputPassword.bind("<KeyRelease>", lambda event: manageVisibility(
        ImageTk, Image, canvasManagePassword, NW, inputPassword, 435, 398
    ))

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

    labelInfo.bind("<Button-1>", lambda event: openSignInLink(event, registerWindow))

    btnRegister = Button(registerWindow, text="Register", font=(
        "Arial", 12, "bold"), bg="#B5960E", fg="white",  cursor="hand2", width=10, height=2)
    # center
    btnRegister.place(x=210, y=570)

    btnRegister.bind("<Button-1>", lambda event: checkRegister(
        inputUsername.get(), inputEmail.get(), inputPassword.get(), inputConfirmPassword.get(), registerWindow))



def checkRegister(username, email, password, confirmPassword, registerWindow):
    
    global isLogged, isRegister

    if (username == "" or email == "" or password == "" or confirmPassword == ""):
        return messagebox.showerror("Error", "All fields are required")

    # check if the username already exists
    elif (checkRegisterUsername(username) == False):
        return messagebox.showerror("Error", "Username already exists")
    
    elif(checkEmail(email) == False):
        return messagebox.showerror("Error", "Invalid email")
    
    # check if the email already exists
    elif (checkRegisterEmail(email) == False):
        return messagebox.showerror("Error", "Email already exists")
    
    elif (password != confirmPassword):
        return messagebox.showerror("Error", "Passwords don't match")
    
    else :
        user = register(username, email, password)

        if (user == True): # if the register function returns True will add the user to the database
            messagebox.showinfo("Success", f"We're glad you join our family Chief {username}")

            isLogged = True
            isRegister = True

            registerWindow.destroy()

            HomeView(user, isLogged, isRegister)


def openSignUpLink(event, loginWindow):
    loginWindow.destroy()
    registerView()

def openSignInLink(event, registerWindow):
    registerWindow.destroy()
    loginView()
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from models.Authenticate import *


def loginView():
    # open the window
    loginWindow = tk.Toplevel()
    loginWindow.title("Login")
    loginWindow.iconbitmap("assets/CraftingCook.ico")
    loginWindow.geometry("580x534")
    loginWindow.resizable(0, 0)
    loginWindow.config(bg="#806B14")

    # canvas
    canvasLogin = Canvas(loginWindow, bg="#806B14", height=534, width=580)
    canvasLogin.place(x=0, y=0)

    canvasLogin.image = tk.PhotoImage(file="assets/images/login_image.png")

    canvasLogin.create_image(0, 0, anchor=NW, image=canvasLogin.image)

    

    loginWindow.grab_set()
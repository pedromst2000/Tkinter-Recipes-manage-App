import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from models.Authenticate import checkLoggedUserRole, checkLoggedUserIsBlocked


def HomeView(user, isLogged):
    
    if (isLogged == True):
        if (checkLoggedUserRole(user["email"]) == "admin"):
            print("admin logged user view") 

        if (checkLoggedUserRole(user["email"]) == "regular" and checkLoggedUserIsBlocked(user["email"]) == True):
            print("regular logged user with blocked acess view")

        elif (checkLoggedUserRole(user["email"]) == "regular"):
            print("regular logged user view")

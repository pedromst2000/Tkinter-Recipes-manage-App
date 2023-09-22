import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from models.Authenticate import checkLoggedUserRole, checkLoggedUserIsBlocked


def HomeView(user, isLogged, isRegister):
    
    if (isLogged == True and isRegister == False):
        if (checkLoggedUserRole(user["email"]) == "admin"):
            print("admin logged user view") ## adminUserHomeView function

        if (checkLoggedUserRole(user["email"]) == "regular" and checkLoggedUserIsBlocked(user["email"]) == True):
            print("regular logged user with blocked acess view") ## blockedUserHomeView function

        elif (checkLoggedUserRole(user["email"]) == "regular"): # regularUserHomeView function
            print("regular logged user view")

    elif(isLogged == True and isRegister == True):
        print("register view regular user") ## regularUserHomeView function
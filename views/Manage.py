from tkinter import Tk, Frame, Canvas, Button, TOP, X, NW, Image, Label, Entry, messagebox, ttk, Toplevel
import tkinter as tk
from classes.Navbar import NavbarWidget
from models.Categories import get_categories, create_category, delete_category
from models.Users import get_user


def ManageView(user, Window):

    manageWindow = Toplevel(Window)

    manageWindow.title("CraftingCook")

    Window.withdraw()

    manageWindow.geometry("1280x650")

    manageWindow.iconbitmap("assets/CraftingCook.ico")

    manageWindow.resizable(0, 0)

    manageWindow.configure(bg="#806B14")

    navbar = NavbarWidget(
        manageWindow,
        "assets/images/Home/notification.png",  # notificationIcon
        "assets/images/Home/exit_app.png",  # exitAppIcon
        user
    )
    navbar.create_widget()

    # open the main window when the profile window is closed
    manageWindow.protocol("WM_DELETE_WINDOW", lambda: [
        manageWindow.destroy(), Window.deiconify()])

    manageWindow.mainloop()

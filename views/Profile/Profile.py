from tkinter import *
from PIL import ImageTk, Image

def ProfileView(Window, user):
    
    # open new window   
    profileWindow = Toplevel(Window)

    profileWindow.title("CraftingCook - Profile")

    # hide the main window
    Window.withdraw()

    profileWindow.geometry("650x650")

    profileWindow.iconbitmap("assets/CraftingCook.ico")

    profileWindow.resizable(0, 0)

    if (user["role"] == "admin"):
        adminProfileView(user)

    elif (user["role"] == "regular"):
        regularProfileView(user)

    # open the main window when the profile window is closed
    profileWindow.protocol("WM_DELETE_WINDOW", lambda: [profileWindow.destroy(), Window.deiconify()])

    profileWindow.mainloop()


def adminProfileView(user):
    print(f"username: {user['username']}")


def regularProfileView(user):
    print(f"username: {user['username']}")
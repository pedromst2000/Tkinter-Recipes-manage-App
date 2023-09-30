from tkinter import *

def ProfileView(Window, user):
    
    # lazy import to avoid circular import error
    from widgets.Avatar import Avatar

    # open new window   
    profileWindow = Toplevel(Window)

    profileWindow.title(f"CraftingCook - Profile - {user['username']}")

    # hide the main window
    Window.withdraw()

    profileWindow.geometry("650x700")

    profileWindow.iconbitmap("assets/CraftingCook.ico")

    profileWindow.resizable(0, 0)

    # background color
    profileWindow.configure(bg="#806B14")

    # avatar
    avatar_widget = Avatar(
        user["avatar"],
        "arrow",
        200,
        200,
        225,
        50,
        200,
        200,
        0,
        0,
        profileWindow,
        user
    )

    # create the avatar widget 
    avatar_widget.create_widget()
    
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
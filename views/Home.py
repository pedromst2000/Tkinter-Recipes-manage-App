from tkinter import messagebox, Tk, Frame, TOP, X, NW, Canvas, Image
from PIL import ImageTk, Image
from models.Users import checkLoggedUserRole, checkLoggedUserIsBlocked
from widgets.Navbar import NavbarWidget
from widgets.HomeCanvas import HomeCanvasWidget


def HomeView(user, isLogged, isRegister):

    if (isLogged == True and isRegister == False):
        if (checkLoggedUserRole(user["email"]) == "admin"):
            adminUserHomeView(user)

        if (checkLoggedUserRole(user["email"]) == "regular" and checkLoggedUserIsBlocked(user["email"]) == True):
            blockedUserHomeView(user)

        elif (checkLoggedUserRole(user["email"]) == "regular"):
            regularUserHomeView(user, isRegister)

    elif (isLogged == True and isRegister == True):
        regularUserHomeView(user, isRegister)


def adminUserHomeView(user):
    Window = Tk()

    Window.title("CraftingCook")
    Window.geometry("1280x650")

    Window.iconbitmap("assets/CraftingCook.ico")

    Window.resizable(0, 0)

    navbar_widget = NavbarWidget(
        Window, 
        user["avatar"], # avatarUser 
        "assets/images/Home/notification.png", # notificationIcon
        "assets/images/Home/exit_app.png", # exitAppIcon
        user
    )
    navbar_widget.create_widget()

    home_canvas_widget = HomeCanvasWidget(
        Window,
        user,
        "assets/images/Home/Manage_icon.png", 
        "assets/images/Home/settings_icon.png",
        "assets/images/Home/recipes_icon.png",
        "assets/images/Home/dashboard_icon.png",
        "assets/images/Home/favorites_icon.png",
        "assets/images/Home/home_image_V2.png"
    )
    home_canvas_widget.create_widget()

    Window.mainloop()


def regularUserHomeView(user, isRegister):
    Window = Tk()

    Window.title("CraftingCook")
    Window.geometry("1280x650")

    Window.iconbitmap("assets/CraftingCook.ico")

    Window.resizable(0, 0)

    navbar_widget = NavbarWidget(
        Window,
        user["avatar"],
        "assets/images/Home/notification.png",
        "assets/images/Home/exit_app.png",
        user
    )
    navbar_widget.create_widget()

    home_canvas_widget = HomeCanvasWidget(
         Window,
        user,
        "assets/images/Home/Manage_icon.png",
        "assets/images/Home/settings_icon.png",
        "assets/images/Home/recipes_icon.png",
        "assets/images/Home/dashboard_icon.png",
        "assets/images/Home/favorites_icon.png",
        "assets/images/Home/home_image_V2.png"
    )
    home_canvas_widget.create_widget()

    if (isRegister == True):
        messagebox.showinfo("Welcome",
                            "1 - You can access your profile throught the avatar\n\n" +
                            "2 - Clicking the notification icon '🔔' will open your notifications\n\n"
                            )

    Window.mainloop()


def blockedUserHomeView(user):
    Window = Tk()

    Window.title("CraftingCook")
    Window.geometry("1280x800")

    Window.iconbitmap("assets/CraftingCook.ico")

    Window.resizable(0, 0)

    # navbar
    navbar = Frame(Window, bg="#E5B714", height=100)
    navbar.pack(side=TOP, fill=X)

    # round canvas for the avatar
    canvasAvatar = Canvas(navbar, height=70, width=70, highlightthickness=0)
    canvasAvatar.place(x=20, y=15)

    # avatar
    avatar = Image.open(user["avatar"])

    avatar = avatar.resize((70, 70))

    avatar = ImageTk.PhotoImage(avatar)

    canvasAvatar.create_image(0, 0, anchor=NW, image=avatar)

    Window.mainloop()

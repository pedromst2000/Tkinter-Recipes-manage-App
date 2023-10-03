from tkinter import Toplevel, Button, Canvas, NW, X, TOP, Frame
from models.Users import change_password, save_avatar, delete_account
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image


def ProfileView(Window, user):

    # open new window
    profileWindow = Toplevel(Window)

    profileWindow.title(f"CraftingCook - Profile - {user['username']}")

    # hide the main window
    Window.withdraw()

    profileWindow.iconbitmap("assets/CraftingCook.ico")

    profileWindow.resizable(0, 0)

    # background color
    profileWindow.configure(bg="#806B14")

    # Profile Avatar
    canvasAvatar = Canvas(profileWindow, height=200, width=200,
                          highlightthickness=0, bg="#E5B714", cursor="arrow")

    canvasAvatar.place(x=225, y=50)

    avatar = Image.open(user["avatar"])

    avatar = avatar.resize((200, 200))

    avatar = ImageTk.PhotoImage(avatar)  # Store as an instance variable

    canvasAvatar.create_image(0, 0, anchor=NW, image=avatar)

    # the size of the window is different depending on the role of the user
    if (user["role"] == "admin"):
        profileWindow.geometry("650x620")

        btnChangeAvatar = Button(
        profileWindow,
        text="Change Avatar",
        font=("Arial", 15),
        bg="#B5960E",
        fg="#FFFFFF",
        bd=0,
        cursor="hand2",
        # change background color when the mouse is over the button
        activebackground="#D1A711",
        # change foreground color when the mouse is over the button
        activeforeground="#ffffff",
        padx=25,
        pady=10
    )
        btnChangeAvatar.place(x=228, y=300)

        btnSaveAvatar = Button(
        profileWindow,
        text="Save Avatar",
        font=("Arial", 15),
        bg="#B5960E",
        fg="#FFFFFF",
        bd=0,
        cursor="hand2",
        # change background color when the mouse is over the button
        activebackground="#D1A711",
        # change foreground color when the mouse is over the button
        activeforeground="#ffffff",
        padx=35,
        pady=10
    )
        btnSaveAvatar.place(x=228, y=400)

        btnPendingAprovals = Button(
        profileWindow,
        text="Pending Aprovals",
        font=("Arial", 15),
        bg="#B5960E",
        fg="#FFFFFF",
        bd=0,
        cursor="hand2",
        # change background color when the mouse is over the button
        activebackground="#D1A711",
        # change foreground color when the mouse is over the button
        activeforeground="#ffffff",
        padx=15,
        pady=10
    )
        btnPendingAprovals.place(x=228, y=500)

    elif (user["role"] == "regular"):
        profileWindow.geometry("650x750")

        btnChangeAvatar = Button(
        profileWindow,
        text="Change Avatar",
        font=("Arial", 15),
        bg="#B5960E",
        fg="#FFFFFF",
        bd=0,
        cursor="hand2",
        # change background color when the mouse is over the button
        activebackground="#D1A711",
        # change foreground color when the mouse is over the button
        activeforeground="#ffffff",
        padx=25,
        pady=10
    )

        btnChangeAvatar.place(x=128, y=300)

        btnSaveAvatar = Button(
        profileWindow,
        text="Save Avatar",
        font=("Arial", 15),
        bg="#B5960E",
        fg="#FFFFFF",
        bd=0,
        cursor="hand2",
        # change background color when the mouse is over the button
        activebackground="#D1A711",
        # change foreground color when the mouse is over the button
        activeforeground="#ffffff",
        padx=35,
        pady=10
    )

        btnSaveAvatar.place(x=128, y=400)

        btnChangePassword = Button(
        profileWindow,
        text="Change Password",
        font=("Arial", 15),
        bg="#B5960E",
        fg="#FFFFFF",
        bd=0,
        cursor="hand2",
        # change background color when the mouse is over the button
        activebackground="#D1A711",
        # change foreground color when the mouse is over the button
        activeforeground="#ffffff",
        padx=15,
        pady=10
    )
        btnChangePassword.place(x=328, y=300)

        btnDeleteAccount = Button(
        profileWindow,
        text="Delete Account",
        font=("Arial", 15),
        bg="#B5960E",
        fg="#FFFFFF",
        bd=0,
        cursor="hand2",
        # change background color when the mouse is over the button
        activebackground="#D1A711",
        # change foreground color when the mouse is over the button
        activeforeground="#ffffff",
        padx=28,
        pady=10
    )

        btnDeleteAccount.place(x=328, y=400)

    # open the main window when the profile window is closed
    profileWindow.protocol("WM_DELETE_WINDOW", lambda: [
                           profileWindow.destroy(), Window.deiconify()])

    profileWindow.mainloop()

from tkinter import Toplevel, Button
from models.Users import change_password, save_avatar, delete_account
from tkinter import messagebox, filedialog

def get_file_extension(filename):
    
        filename = filename.split(".")
    
        return filename[len(filename) - 1]


def changeAvatar(profileWindow, user):

      # lazy import to avoid circular import error
    from widgets.Avatar import Avatar

    # open the file explorer
    filename = filedialog.askopenfilename(
        title="Select an image",
        filetypes=(
            ("png files", "*.png"),
            ("jpg files", "*.jpg"),
            ("jpeg files", "*.jpeg")
        )
    )

    # get the file extension
    file_extension = get_file_extension(filename)

    # if the file is an image
    if (file_extension in ["png", "jpg", "jpeg"]):
        print(filename)
     
     
    else:
        messagebox.showerror(
            "Error", "The file must be an image with the extension png, jpg or jpeg")


def ProfileView(Window, user):

    # lazy import to avoid circular import error
    from widgets.Avatar import Avatar

    # open new window
    profileWindow = Toplevel(Window)

    profileWindow.title(f"CraftingCook - Profile - {user['username']}")

    # hide the main window
    Window.withdraw()

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
        profileWindow.geometry("650x620")
        adminProfileView(profileWindow, user)

    elif (user["role"] == "regular"):
        profileWindow.geometry("650x750")
        regularProfileView(profileWindow, user)


    profileWindow.iconbitmap("assets/CraftingCook.ico")

    profileWindow.resizable(0, 0)

    # background color
    profileWindow.configure(bg="#806B14")

    # open the main window when the profile window is closed
    profileWindow.protocol("WM_DELETE_WINDOW", lambda: [
                           profileWindow.destroy(), Window.deiconify()])

    profileWindow.mainloop()


def adminProfileView(profileWindow, user):
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

    btnChangeAvatar.bind("<Button-1>", lambda event: changeAvatar())

    # bind - onClick will call the save avatar
    btnSaveAvatar.bind("<Button-1>", lambda event: save_avatar(
        user["email"], 
            changeAvatar()
        ))


def regularProfileView(profileWindow, user):

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

    btnChangeAvatar.bind("<Button-1>", lambda event: changeAvatar(profileWindow, user))

    # btnSaveAvatar.bind("<Button-1>", lambda event: save_avatar(
    #     user["email"], 
    #     "chief.png"
    #     ))

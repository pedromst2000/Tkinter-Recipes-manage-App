from tkinter import Toplevel, Button, Canvas, NW, X, TOP, Frame
from models.Users import save_avatar, delete_account, get_user
from views.Profile.ChangePassword import changePassword
from tkinter import messagebox, filedialog
import os
from PIL import ImageTk, Image

# global variables for the image and the photo_image
image = ""
photo_image = ""


def changeAvatar(canvasAvatar):

    global image, photo_image

    # open the file dialog
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select an image", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("jpeg files", "*.jpeg")))

    image_path = filename

    image = Image.open(image_path)

    image = image.resize((200, 200))

    photo_image = ImageTk.PhotoImage(image)  # Store as an instance variable

    canvasAvatar.create_image(0, 0, anchor=NW, image=photo_image)

    image = image_path  # assigning the global variable image to the image_path

def saveAvatar(user):

    global image

    # delete any directory path before the image name with slice
    # eg: assets/images/Profile/avatar.png -> avatar.png # the +1: is to remove the / from the path
    avatar = image[image.rindex("/")+1:]

    # join the path of the avatar with the path of the profile folder
    save_path = os.path.join("assets/images/Profile", os.path.basename(avatar))

    with open(image, "rb") as file:
        content = file.read()

        with open(save_path, "wb") as file:
            file.write(content)
        messagebox.showinfo(
            "Success", "Avatar saved successfully, restart the app to see the changes")

        save_avatar(user["email"], avatar)  # save the avatar in the database)

        file.close()

def deleteAccount(user, profileWindow, Window):

    confirmDelete = messagebox.askyesno(
        "Confirm", "Are you sure you want to delete your account?")
    
    if confirmDelete:
        delete_account(user["email"])

        messagebox.showinfo("Success", "Account deleted successfully")

        profileWindow.destroy()

        Window.destroy()


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

    avatar = Image.open(get_user(user["email"])["avatar"])

    avatar = avatar.resize((200, 200))

    avatar = ImageTk.PhotoImage(avatar)  # Store as an instance variable

    canvasAvatar.create_image(0, 0, anchor=NW, image=avatar)

    # the size of the window is different depending on the role of the user
    # conditionally rendering the actions of the profile window depending on the role of the user
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
         # bind - onCLick will call the deleteAccount function
        btnDeleteAccount.bind(
        "<Button-1>", lambda event: deleteAccount(user, profileWindow, Window))
            # bind - onCLick will call the changePassword function
        btnChangePassword.bind("<Button-1>", lambda event: changePassword(user))

    # bind - onCLick will call the changeAvatar function
    btnChangeAvatar.bind(
        "<Button-1>", lambda event: changeAvatar(canvasAvatar))

    # bind - onCLick will call the saveAvatar function
    btnSaveAvatar.bind("<Button-1>", lambda event: saveAvatar(user))

    # open the main window when the profile window is closed
    profileWindow.protocol("WM_DELETE_WINDOW", lambda: [
                           profileWindow.destroy(), Window.deiconify()])
    profileWindow.mainloop()

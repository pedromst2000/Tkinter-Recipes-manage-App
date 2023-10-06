from tkinter import Toplevel, Button, Canvas, NW
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image
from models.Users import change_password
from utils import togglePasswordVisibility, manageVisibility


def changePassword(user):

    # open the window to change the password
    changePasswordWindow = Toplevel()

    changePasswordWindow.title(
        "CraftingCook - Change Password")

    changePasswordWindow.iconbitmap("assets/CraftingCook.ico")

    changePasswordWindow.geometry("560x540")

    changePasswordWindow.resizable(0, 0)

    changePasswordWindow.configure(bg="#806B14")

    canvasChangePassword = Canvas(changePasswordWindow,  height=160,
                                  width=180, highlightthickness=0)

    canvasChangePassword.place(x=200, y=50)

    changePasswordImage = Image.open(
        "assets/images/Authentication/auth_image.png")
    changePasswordImage = changePasswordImage.resize((180, 160))

    changePasswordImage = ImageTk.PhotoImage(changePasswordImage)

    canvasChangePassword.create_image(
        0, 0, anchor=NW, image=changePasswordImage)

    labelNewPassword = tk.Label(changePasswordWindow, text="New Password", font=(
        "Arial", 12, "bold"), bg="#806B14", fg="white")
    labelNewPassword.place(x=120, y=250)

    inputNewPassword = tk.Entry(changePasswordWindow, width=38, font=(
        "Arial", 11, "bold"), bg="white", fg="#806B14", bd=0,  show="*")
    inputNewPassword.place(x=120, y=280)

    labelConfirmPassword = tk.Label(changePasswordWindow, text="Confirm Password", font=(
        "Arial", 12, "bold"), bg="#806B14", fg="white")
    labelConfirmPassword.place(x=120, y=320)

    inputConfirmPassword = tk.Entry(changePasswordWindow, width=38, font=(
        "Arial", 11, "bold"), bg="white", fg="#806B14", bd=0, show="*")
    inputConfirmPassword.place(x=120, y=350)

    btnSave = Button(changePasswordWindow, text="Save", font=(
        "Arial", 12, "bold"), bg="#B5960E", fg="white",  cursor="hand2", width=10, height=2)
    # center
    btnSave.place(x=210, y=420)

    canvasManagePassword = Canvas(changePasswordWindow,  height=26,
                                  width=40, highlightthickness=0, cursor="hand2")

    canvasManagePassword.config(highlightthickness=0, bd=0, bg="#806B14")

    # bind - when the user clicks (onClick) on the canvas, the function will be called
    canvasManagePassword.bind("<Button-1>", lambda event: togglePasswordVisibility(
        ImageTk, Image, canvasManagePassword, NW, inputNewPassword, 435, 280
    ))

    # bind - when the user releases the key (onKeyPress), the function will be called
    inputNewPassword.bind("<KeyRelease>", lambda event: manageVisibility(
        ImageTk, Image, canvasManagePassword, NW, inputNewPassword, 435, 280
    ))

    # onCLick will call the checkChangePassword function
    btnSave.bind("<Button-1>", lambda event: checkChangePassword(
        inputNewPassword.get(), inputConfirmPassword.get(), user, changePasswordWindow))

    changePasswordWindow.mainloop()



def checkChangePassword(newPassword, confirmPassword, user, changePasswordWindow):

    if(newPassword == "" and confirmPassword == ""):
        return messagebox.showerror("Error", "Please fill in all the fields")
    
    if(newPassword != confirmPassword):
        return messagebox.showerror("Error", "The passwords don't match")
    
    else:
        if(change_password(user["email"], newPassword)):
            messagebox.showinfo("Success", "The password was changed successfully")

            changePasswordWindow.destroy()

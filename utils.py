import re as regex

isPasswordVisible = False

# this function will check if the email is valid with regex
# Regex explanation:
# [^@]+ - matches any character except @ one or more times
# @ - matches @ literally
# [^@]+ - matches any character except @ one or more times
# \. - matches . literally
# [^@]+ - matches any character except @ one or more times
def checkEmail(email):

    if (not regex.match(r"[^@]+@[^@]+\.[^@]+", email)):
        return False # if dont match the pattern, return False

    return True # if match the pattern, return True


def hidePasswordIcon(ImageTk, Image, canvasManagePassword, NW, X, Y):
    eye = Image.open("assets/images/hidden_password.png")

    eye = eye.resize((40, 26))

    canvasManagePassword.image = ImageTk.PhotoImage(eye)

    canvasManagePassword.create_image(
        0, 0, anchor=NW, image=canvasManagePassword.image)

    # canvasManagePassword.place(x=435, y=348)
    canvasManagePassword.place(x=X, y=Y)

def showPasswordIcon(ImageTk, Image, canvasManagePassword, NW, X, Y):
    eye = Image.open("assets/images/visible_password.png")

    eye = eye.resize((40, 26))

    canvasManagePassword.image = ImageTk.PhotoImage(eye)

    canvasManagePassword.create_image(
        0, 0, anchor=NW, image=canvasManagePassword.image)

    # canvasManagePassword.place(x=435, y=348)
    canvasManagePassword.place(x=X, y=Y)


# this function will toggle the password visibility and change the icon as well
def togglePasswordVisibility(ImageTk, Image, canvasManagePassword, NW, inputPassword, X, Y): # X and Y are the coordinates of the canvas

    global isPasswordVisible

    if (isPasswordVisible == False): # if the password is not visible
        inputPassword.config(show="") # show the password
        isPasswordVisible = True # change the variable to True
        showPasswordIcon(
            ImageTk, Image, canvasManagePassword, NW, X, Y # X and Y are the coordinates of the canvas
        )
    else:
        inputPassword.config(show="*")
        isPasswordVisible = False
        hidePasswordIcon(
            ImageTk, Image, canvasManagePassword, NW, X, Y
        )

# this function will manage the visibility of the password
def manageVisibility(ImageTk, Image, canvasManagePassword, NW, inputPassword, X, Y):
    
    global isPasswordVisible
    
    if (inputPassword.get() != ""):  # if the password input is not empty
        if (isPasswordVisible == False): # and if the password is not visible
            hidePasswordIcon( # will display the hide password icon
                ImageTk, Image, canvasManagePassword, NW, X, Y 
            )
        if (isPasswordVisible == True): # and if the password is visible
            showPasswordIcon( # will display the show password icon
                ImageTk, Image, canvasManagePassword, NW, X, Y
            )
    else:
        canvasManagePassword.place_forget() # if the password input is empty, the canvas will be hidden and not showing any icon (either hide or show password icon)

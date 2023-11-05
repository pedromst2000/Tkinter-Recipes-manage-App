from tkinter import Tk, Frame, Canvas, Button, TOP, X, NW, Image, Label, Entry, messagebox, ttk, Toplevel
import tkinter as tk
from classes.Navbar import NavbarWidget
from models.Categories import get_categories, create_category, delete_category, checkCategory
from models.Users import get_user


def AddCategory(inputCategory, treeview):

    # get the tag and the category from the input fields
    category = inputCategory.get()

    if(category == ""):
         messagebox.showerror("Error", "Please fill all the fields")
    
    # checking if the category already exists
    if(checkCategory(category) == True):
        messagebox.showerror("Error", "The category already exists")    
    
    else:
        # create the category
        create_category(category) ## add the category in the database

        # insert the category in the treeview
        treeview.insert("", tk.END, values=(category))

        messagebox.showinfo("Success", "Category added successfully")

        # clear the input fields
        inputCategory.delete(0, tk.END)

def RemoveCategory(treeview):
    
    # check if the user selected a category
    if treeview.selection():
            
            # get the category selected
            category = treeview.item(treeview.selection()[0])["values"]
    
            # delete the category from the database
            delete_category(category[0], category[1])
    
            # delete the category from the treeview
            treeview.delete(treeview.selection()[0])
    
            messagebox.showinfo("Success", "Category deleted successfully")
        
    else:
        messagebox.showerror("Error", "Please select a category")

def ManageView(user, Window):

    manageWindow = Toplevel(Window)

    categories = get_categories()

    manageWindow.title("CraftingCook - Manage")

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

    btnDeleteCategory = Button(
        manageWindow,
        text="Delete Category",
        font=("Arial", 12, "bold"),
        bg="#B5960E",
        fg="white",
        cursor="hand2",
        width=15,
        height=1,
        activebackground="#D1A711",
        activeforeground="#ffffff",
        bd=2,
        padx=2,
        pady=2,
    )

    btnDeleteCategory.place(x=100, y=125)

    # treeview to display the categories columns  'Category'
    treeview = ttk.Treeview(manageWindow, columns=("Category"), show="headings", height=10)

    treeview.column("Category", anchor=tk.CENTER, width=130)

    treeview.heading("Category", text="Category", anchor=tk.CENTER)
    
    treeview.place(x=50, y=190)

    # scrollbar
    scrollbar = ttk.Scrollbar(manageWindow, orient="vertical")
    scrollbar.configure(command=treeview.yview)
    treeview.configure(yscrollcommand=scrollbar.set)
    scrollbar.place(x=310, y=192, height=224)

    # insert the categories in the treeview
    for category in categories:
        treeview.insert("", tk.END, values=(category["category"]))

    # label for the category
    lblCategory = Label(
        manageWindow,
        text="Category",
        font=("Arial", 12, "bold"),
        bg="#806B14",
        fg="#ffffff"
    )
    lblCategory.place(x=120, y=490)

    # entry for the category
    inputCategory = Entry(
        manageWindow,
        font=("Arial", 12, "bold"),
        bg="#ffffff",
        fg="#806B14",
        bd=0,
        width=15
    )
    inputCategory.place(x=120, y=516)

    btnAddCategory = Button(
        manageWindow,
        text="Add Category",
        font=("Arial", 12, "bold"),
        bg="#B5960E",
        fg="white",
        cursor="hand2",
        width=15,
        height=1,
        activebackground="#D1A711",
        activeforeground="#ffffff",
        bd=2,
        padx=2,
        pady=2,
    )

    # place the button aboce the input fields
    btnAddCategory.place(x=105, y=570)

    # bind the button Onclick event to the AddCategory function
    btnAddCategory.bind("<Button-1>", lambda event: AddCategory(inputCategory, treeview))

    btnDeleteCategory.bind("<Button-1>", lambda event: RemoveCategory(treeview))

    # open the main window when the profile window is closed
    manageWindow.protocol("WM_DELETE_WINDOW", lambda: [
        manageWindow.destroy(), Window.deiconify()])

    manageWindow.mainloop()

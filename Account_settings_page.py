# ---------------------------------------------------------------------------------------------------------------------
# Imports
# import os
from tkinter import *
# from PIL import Image, ImageTk

# ---------------------------------------------------------------------------------------------------------------------
# Roots
root = Tk()
# root.geometry('400x650')
root.title("Account Settings")


# ---------------------------------------------------------------------------------------------------------------------
# Functions
def profile_details():
    print('profile Details')
    import Profile_details_page
    # from Signup_page import DIC_username, DIC_password


def change_password():
    print('change password')
    import Change_pass_page


def logout():
    print('log out')
    import Login_page


def tnc():
    print('Terms and Conditions')


def goback():
    print('Go back')
    root.destroy()
    import Home_page


# ---------------------------------------------------------------------------------------------------------------------
# Frames
Frm_logo = Frame(root)
Frm_logo.pack()

Frm_button = Frame(root)
Frm_button.pack()

# ---------------------------------------------------------------------------------------------------------------------
# Widgets
'''
img = ImageTk.PhotoImage(Image.open("rndm_image.jpg"))  # PIL solution
Label(Frm_logo, image=img, bg='#d3f0ee').pack()
'''
Button(Frm_button, text='Profile Details', width=30, command=profile_details).pack(pady=5)
Button(Frm_button, text='Change Password', width=30, command=change_password).pack(pady=5)
Button(Frm_button, text='Log Out', width=30, command=logout).pack(pady=5)
Button(Frm_button, text='Terms and Conditions', width=30, command=tnc).pack(pady=5)
Button(Frm_button, text='Go Back', width=30, command=goback).pack(pady=5)

# ---------------------------------------------------------------------------------------------------------------------

root.mainloop()

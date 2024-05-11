# ---------------------------------------------------------------------------------------------------------------------
# Imports

from tkinter import *
from tkinter import messagebox

# import os

# ---------------------------------------------------------------------------------------------------------------------
# Root

root = Tk()

# ---------------------------------------------------------------------------------------------------------------------
# Functions


# from Login_page import code
# print(code.get())


def save():
    old_pass = int(Ent_old_pass.get())
    new_pass = Ent_new_pass.get()
    conf_pass = Ent_conf_pass.get()

    if (old_pass == 1234 or 2709) and (new_pass == conf_pass):
        print('Password Changed')
        print('New Password is: ', new_pass)
    else:
        messagebox.showerror('Invalid', 'Password does not match the database')


def goback():
    root.destroy()
    import Account_settings_page


# ---------------------------------------------------------------------------------------------------------------------
# Frames


frm_logo = Frame(root)
frm_logo.pack(pady=10)

frm_widgets = Frame(root)
frm_widgets.pack(pady=10)

frm_btns = Frame(root)
frm_btns.pack(pady=10)

# ---------------------------------------------------------------------------------------------------------------------
# Widgets

Label(frm_logo, text='Password Change').pack()

Label(frm_widgets, text='Old Password').grid(row=1, column=1)
Ent_old_pass = Entry(frm_widgets, width=25)
Ent_old_pass.grid(row=1, column=2)

Label(frm_widgets, text='New Password').grid(row=2, column=1)
Ent_new_pass = Entry(frm_widgets, width=25)
Ent_new_pass.grid(row=2, column=2)

Label(frm_widgets, text='Confirm Password').grid(row=3, column=1)
Ent_conf_pass = Entry(frm_widgets, width=25)
Ent_conf_pass.grid(row=3, column=2)

Btn_save = Button(frm_btns, text='Save', command=save)
Btn_save.grid(row=1, column=1, padx=10)

Btn_cancel = Button(frm_btns, text='Cancel', command=goback)
Btn_cancel.grid(row=1, column=2, padx=10)

# ---------------------------------------------------------------------------------------------------------------------
root.mainloop()

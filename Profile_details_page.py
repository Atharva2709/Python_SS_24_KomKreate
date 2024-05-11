# ---------------------------------------------------------------------------------------------------------------------
# Imports
from tkinter import *
# import os

# ---------------------------------------------------------------------------------------------------------------------
# Root
root = Tk()


# ---------------------------------------------------------------------------------------------------------------------
# Functions


def save():
    Ent_email.config(state='readonly')
    Ent_username.config(state='readonly')
    Ent_name.config(state='readonly')


def edit():
    Ent_email.config(state='normal')
    Ent_username.config(state='normal')
    Ent_name.config(state='normal')


def goback():
    root.destroy()
    import Account_settings_page


# ---------------------------------------------------------------------------------------------------------------------
# Frames
frm_1 = Frame(root)
frm_1.pack(pady=10)

frm_2 = Frame(root)
frm_2.pack(pady=10)

# ---------------------------------------------------------------------------------------------------------------------
# Widgets
Lbl_title = Label(frm_1, text='Logo')
Lbl_title.pack()


'''
Lbl_weight1 = Label(frm_2, text='')
Lbl_weight1.grid(row=1, column=2)
frm_2.rowconfigure(0, weight=1)
'''

Lbl_details = Label(frm_2, text='Details')
Lbl_details.grid(row=1, column=2)

Btn_edit = Button(frm_2, text='Edit', bd=0, font='blue', command=edit)
Btn_edit.grid(row=2, column=3)

Label(frm_2, text='Email').grid(row=3, column=1)
Ent_email = Entry(frm_2, width=25)
Ent_email.grid(row=3, column=2)

Label(frm_2, text='Username').grid(row=4, column=1)
Ent_username = Entry(frm_2, width=25)
Ent_username.grid(row=4, column=2)

Label(frm_2, text='Name').grid(row=5, column=1)
Ent_name = Entry(frm_2, width=25)
Ent_name.grid(row=5, column=2)

Btn_save = Button(frm_2, text='Save', command=save)
Btn_save.grid(row=6, column=2)

Btn_goback = Button(frm_2, text='Go Back', command=goback)
Btn_goback.grid(row=6, column=3)

root.mainloop()

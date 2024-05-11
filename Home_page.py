# ---------------------------------------------------------------------------------------------------------------------
# Imports
# import os
from tkinter import *
from datetime import datetime
from datetime import date
from PIL import Image, ImageTk

# import Login_page

# ---------------------------------------------------------------------------------------------------------------------
# Roots

root = Tk()

# ---------------------------------------------------------------------------------------------------------------------
# Frames

frm_logo = Frame(root)
frm_logo.pack(pady=5)
frm_logo.rowconfigure(0, weight=1)
frm_logo.columnconfigure(0, weight=1)

frm_widgets = Frame(root)
frm_widgets.pack(pady=5)
frm_widgets.rowconfigure(0, weight=1)
frm_widgets.columnconfigure(0, weight=1)

# ---------------------------------------------------------------------------------------------------------------------
# Functions

# print(username)
# welcome_username = ('Welcome', username)

today_date = date.today()
time = datetime.now().strftime("%H:%M")
date_time = (today_date, time)


def add_sales():
    root.destroy()
    import Add_sales


def global_sales():
    root.destroy()
    import Global_sales_page


def acc_settings():
    root.destroy()
    import Account_settings_page

# ---------------------------------------------------------------------------------------------------------------------
# Widgets


# Logo Frame

img = ImageTk.PhotoImage(Image.open("rndm_image.jpg"))  # PIL solution
Label(frm_logo, image=img, bg='#d3f0ee').pack(pady=10, padx=10)

# Label(frm_logo, text='LOGO').pack(pady=10)

# Widgets Frame
Lbl_welcome = Label(frm_widgets, text='welcome')
Lbl_welcome.grid(row=0, column=0)

Lbl_date_time = Label(frm_widgets, text=date_time)
Lbl_date_time.grid(row=0, column=2)

Btn_add_sales = Button(frm_widgets, text='Add Sales', width=30, command=add_sales)
Btn_add_sales.grid(row=1, column=1, pady=5)

Btn_global_sales = Button(frm_widgets, text='Global Sales', width=30, command=global_sales)
Btn_global_sales.grid(row=2, column=1, pady=5)

Btn_account_settings = Button(frm_widgets, text='Account Settings', width=30, command=acc_settings)
Btn_account_settings.grid(row=3, column=1, pady=5)

# ---------------------------------------------------------------------------------------------------------------------

root.mainloop()

from tkinter import *
from tkinter import messagebox
# import os

import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title('Sales Chart Page')

DIC_month_number = []
DIC_goal = []
DIC_sales = []
month = ["January", "February", "March",
         "April", "May", "June",
         "June", "July", "August",
         "September", "October", "November", "December"]

frm_1 = Frame(root)
frm_1.grid(row=1, column=1)

frm_2 = Frame(root)
frm_2.grid(row=2, column=1)

frm_3 = Frame(root)
frm_3.grid(row=3, column=1)

frm_4 = Frame(root)
frm_4.grid(row=4, column=1)

i = 2


# ---------------------------------------------------------------------------------------------------------------------
# Functions


def new_ent():
    month_number = month_selected.get()
    if month_number == "January":
        month_number = 1
        DIC_month_number.append(month_number)
    elif month_number == "February":
        month_number = 2
        DIC_month_number.append(month_number)
    elif month_number == "March":
        month_number = 3
        DIC_month_number.append(month_number)
    elif month_number == "April":
        month_number = 4
        DIC_month_number.append(month_number)
    elif month_number == "May":
        month_number = 5
        DIC_month_number.append(month_number)
    elif month_number == "June":
        month_number = 6
        DIC_month_number.append(month_number)
    elif month_number == "July":
        month_number = 7
        DIC_month_number.append(month_number)
    elif month_number == "August":
        month_number = 8
        DIC_month_number.append(month_number)
    elif month_number == "September":
        month_number = 9
        DIC_month_number.append(month_number)
    elif month_number == "October":
        month_number = 10
        DIC_month_number.append(month_number)
    elif month_number == "November":
        month_number = 11
        DIC_month_number.append(month_number)
    elif month_number == "December":
        month_number = 12
        DIC_month_number.append(month_number)
    else:
        messagebox.showerror("Invalid", "Invalid Month")

    # user_goal = Ent_goal.get()
    DIC_goal.append(Ent_goal.get())
    Ent_goal.delete(0, 'end')
    # user_sales = Ent_sales.get()
    DIC_sales.append(Ent_sales.get())
    Ent_sales.delete(0, 'end')


def plot():
    # fig, ax = plt.subplots()
    # canvas = FigureCanvasTkAgg(fig, master=frm_3)

    # ax.clear()

    # ax.plot(DIC_month_number, DIC_sales)
    # ax.plot(DIC_month_number, DIC_goal)
    plt.plot(DIC_month_number, DIC_goal, color='r', marker='.', label='Ideal Sales')
    plt.plot(DIC_month_number, DIC_sales, color='b', marker='.', label='Sales by Atharva')

    # canvas.draw()
    # canvas.get_tk_widget().grid(row=1, column=1)
    # toolbar = NavigationToolbar2Tk(canvas, frm_3, pack_toolbar=False)
    # toolbar.update()
    # toolbar.grid(row=2, column=1)

    plt.xlabel('Months')
    plt.ylabel('Sales (EUR)')
    plt.title('Median Sales (EUR) by Months')

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    for element in DIC_month_number:
        print(element)
    for element in DIC_goal:
        print(element)
    for element in DIC_sales:
        print(element)


def comment_send():
    # ent_comment.insert(0)
    # ent_comment.delete(0, 'end')
    received_comments = ent_comment.get()
    frm_comments = Frame(frm_4)
    frm_comments.grid(row=2, column=1, columnspan=3)
    Label(frm_comments, text="Comments!").grid(row=1, column=1)
    comments = Label(frm_comments, text=received_comments)
    comments.grid(row=3, column=1)
    ent_comment.delete(0, 'end')


def homepage():
    plt.close()
    root.destroy()
    import Home_page


# ---------------------------------------------------------------------------------------------------------------------
# Frame 1

Label(frm_1, text="Month").grid(row=1, column=1)
month_selected = StringVar()
month_selected.set("Choose Month")
OptMenu_month = OptionMenu(frm_1, month_selected, *month)
OptMenu_month.grid(row=1, column=2)

Label(frm_1, text="User Goal").grid(row=1, column=3)
Ent_goal = Entry(frm_1, width=25)
Ent_goal.grid(row=1, column=4)

Label(frm_1, text="User Sale").grid(row=1, column=5)
Ent_sales = Entry(frm_1, width=25)
Ent_sales.grid(row=1, column=6)

# ---------------------------------------------------------------------------------------------------------------------
# Frame 2

Btn_get = Button(frm_2, text="Get it!", command=new_ent)
Btn_get.grid(row=1, column=1, pady=10, padx=10)

Btn_graph = Button(frm_2, text="Graph it!", command=plot)
Btn_graph.grid(row=1, column=2, pady=10, padx=10)

Btn_close = Button(frm_2, text="Close!", command=homepage)
Btn_close.grid(row=1, column=3, pady=10, padx=10)

# ---------------------------------------------------------------------------------------------------------------------
# Frame 3
# In the Function

# ---------------------------------------------------------------------------------------------------------------------
# Frame 4

lbl_comment = Label(frm_4, text="Comment?")
lbl_comment.grid(row=1, column=1)

ent_comment = Entry(frm_4, width=100)
ent_comment.grid(row=1, column=2)

Btn_comment = Button(frm_4, text="Send!", command=comment_send)
Btn_comment.grid(row=1, column=3)

# ---------------------------------------------------------------------------------------------------------------------

root.mainloop()

from matplotlib import pyplot as plt
import random
from tkinter import *
from tkinter import messagebox
# import os


root = Tk()


def get_sales():
    if 1950 < int(Ent_year.get()) < 2024:
        bot_month_number = []
        bot_goal = []
        bot_sales = []
        i = 1

        while i <= 12:
            month_number = i
            bot_month_number.append(month_number)
            goal = random.randint(5000, 35000)
            bot_goal.append(goal)
            sales = random.randint(5000, 50000)
            bot_sales.append(sales)
            i = i + 1

        for element in bot_month_number:
            print(element)
        for element in bot_goal:
            print(element)
        for element in bot_sales:
            print(element)

        plt.plot(bot_month_number, bot_goal, color='k', linestyle='--', marker='.', label='Ideal Global Sales')
        plt.plot(bot_month_number, bot_sales, color='b', marker='.', label='Actual Global Sales')

        plt.xlabel('Months')
        plt.ylabel('Sales (EUR)')
        plt.title('Median Sales (EUR) by Months')

        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    elif int(Ent_year.get()) == 2024:
        bot_month_number = []
        bot_goal = []
        bot_sales = []
        i = 1

        while i <= 5:
            month_number = i
            bot_month_number.append(month_number)
            goal = random.randint(5000, 35000)
            bot_goal.append(goal)
            sales = random.randint(5000, 50000)
            bot_sales.append(sales)
            i = i + 1

        for element in bot_month_number:
            print(element)
        for element in bot_goal:
            print(element)
        for element in bot_sales:
            print(element)

        plt.plot(bot_month_number, bot_goal, color='k', linestyle='--', marker='.', label='Ideal Global Sales')
        plt.plot(bot_month_number, bot_sales, color='b', marker='.', label='Actual Global Sales')

        plt.xlabel('Months')
        plt.ylabel('Sales (EUR)')
        plt.title('Median Sales (EUR) by Months')

        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    else:
        messagebox.showerror('Wrong Year', 'We cant predict the future (yet)!')


def homepage():
    root.destroy()
    import Home_page


Label(root, text='Global Sales', font=18).pack()

frm_year = Frame(root)
frm_year.pack(pady=10)

Ent_year = Entry(frm_year)
Ent_year.pack(padx=10)

Btn_get_sales = Button(frm_year, text='Get Sales', command=get_sales)
Btn_get_sales.pack(pady=5)

Btn_goback = Button(root, text='Homepage', command=homepage)
Btn_goback.pack(pady=+10)


root.mainloop()

from tkinter import *
# import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

root = Tk()
root.title('Sales Chart Page')

dev_month_number = []
dev_goal = []
dev_sales = []
# bot_goal = []
# bot_sales = []


def new_ent():
    month_number = Ent_month.get()
    dev_month_number.append(month_number)
    Ent_month.delete(0, 'end')
    user_goal = Ent_goal.get()
    dev_goal.append(user_goal)
    Ent_goal.delete(0, 'end')
    user_sales = Ent_sales.get()
    dev_sales.append(user_sales)
    Ent_sales.delete(0, 'end')
    # b_sales = random.randint(5000, 25000)
    # bot_sales.append(b_sales)
    # b_goal = random.randint(5000, 25000)
    # bot_goal.append(b_goal)


def plot():
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)

    ax.clear()

    ax.plot(dev_month_number, dev_sales, linestyle="-")
    ax.plot(dev_month_number, dev_goal, linestyle="--")
    # ax.plot(dev_month_number, bot_sales, linestyle="-.")
    # ax.plot(dev_month_number, bot_goal, linestyle=":")
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(anchor="w", fill=X)


frm_1 = Frame(root)
frm_1.pack()

Label(frm_1, text="Month").grid(row=0, column=0)
Ent_month = Entry(frm_1, width=25)
Ent_month.grid(row=0, column=1)

Label(frm_1, text="User Goal").grid(row=1, column=0)
Ent_goal = Entry(frm_1, width=25)
Ent_goal.grid(row=1, column=1)

Label(frm_1, text="User Sale").grid(row=2, column=0)
Ent_sales = Entry(frm_1, width=25)
Ent_sales.grid(row=2, column=1)

Btn_graph = Button(root, text="Graph it!", command=plot)
Btn_graph.pack(pady=10)

Btn_get = Button(root, text="Get it!", command=new_ent)
Btn_get.pack(pady=10)

Btn_close = Button(root, text="Close!", command=root.destroy)
Btn_close.pack(pady=10)

root.mainloop()

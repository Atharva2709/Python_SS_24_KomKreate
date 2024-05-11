# ----------------------------------------------------------------------------------------------------------------------
# Imports
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

# import os

# ----------------------------------------------------------------------------------------------------------------------
# Window Settings

login_root = Tk()
login_root.title("Log in")
login_root.geometry('925x500+300+200')
login_root.configure(bg="#d3f0ee")
login_root.resizable(False, False)


# ----------------------------------------------------------------------------------------------------------------------
# Functions

def signin():
    # from Signup_page import DIC_username, DIC_password
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '1234':
        print('Logged In with admin')
        import Home_page
    elif username == 'Atharva' and password == '2709':
        print('Logged in with you')
        import Home_page
    elif (username != 'admin' and password != '1234') or (username != 'Atharva' and password != '2709'):
        from Signup_page import DIC_username, DIC_password
        if password == DIC_password[DIC_username.index(username)]:
            print('Logged in with user')
            import Home_page
        else:
            messagebox.showerror("Invalid", "Invalid Username or Password")
    elif username != 'Username' and password != 'Password':
        messagebox.showerror("Invalid", "Invalid Username or Password")
    else:
        messagebox.showerror("Invalid", "Invalid Username or Password")


def u_on_enter(e):
    user.delete(0, 'end')


def u_on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


def p_on_enter(e):
    code.delete(0, 'end')


def p_on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


def hide():
    openeye_img.config(file='closeye.png')
    code.config(show='*')
    Btn_eye.config(command=show)


def show():
    openeye_img.config(file='openeye.png')
    code.config(show='')
    Btn_eye.config(command=hide)


def signup():
    print("Signup Page")
    login_root.destroy()
    import Signup_page


# ----------------------------------------------------------------------------------------------------------------------
# Widgets

frm_1 = Frame(login_root)
frm_1.place(x=120, y=120)
# img = ImageTk.PhotoImage(Image.open("rndm_image.jpg"))  # PIL solution
# Label(frm_1, image=img, bg='#d3f0ee').pack()

Signin_frame = Frame(login_root, width=350, height=350, bg='white')
Signin_frame.place(x=480, y=70)

Signin_heading = Label(Signin_frame, text="Sign in", fg="#57a1f8", bg="white",
                       font=('Microsoft Yahei UI Light', 23, 'bold'))
Signin_heading.place(x=115, y=5)

user = Entry(Signin_frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', u_on_enter)
user.bind('<FocusOut>', u_on_leave)
Frame(Signin_frame, width=295, height=2, bg='black').place(x=25, y=107)

code = Entry(Signin_frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', p_on_enter)
code.bind('<FocusOut>', p_on_leave)
Frame(Signin_frame, width=295, height=2, bg='black').place(x=25, y=177)

openeye_img = PhotoImage(file='openeye.png')
Btn_eye = Button(Signin_frame, image=openeye_img, bd=0, bg='white', activebackground='white', cursor='Heart',
                 command=hide)
Btn_eye.place(x=290, y=150)

Button(Signin_frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=2, command=signin).place(x=35,
                                                                                                                 y=204)
label = Label(Signin_frame, text="Dont have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(Signin_frame, width=6, text='Sign Up', border=0, bg='white', cursor='hand2', fg='#57a1f8',
                 command=signup)
sign_up.place(x=215, y=270)

# ----------------------------------------------------------------------------------------------------------------------
# Main-loops

login_root.mainloop()

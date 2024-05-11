# ----------------------------------------------------------------------------------------------------------------------
# Imports
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

# ----------------------------------------------------------------------------------------------------------------------
# Window Settings

signup_root = Tk()
signup_root.title("Sign Up")
signup_root.geometry('925x500+300+200')
signup_root.configure(bg="#d3f0ee")
signup_root.resizable(False, False)

# ----------------------------------------------------------------------------------------------------------------------
# Functions

DIC_username = []
DIC_password = []
var = IntVar()


def e_on_enter(event):
    Ent_email.delete(0, 'end')


def e_on_leave(event):
    email = Ent_email.get()
    if email == '':
        Ent_email.insert(0, 'Email')


def u_on_enter(event):
    Ent_username.delete(0, 'end')


def u_on_leave(event):
    username = Ent_username.get()
    if username == '':
        Ent_username.insert(0, 'Username')


def p_on_enter(event):
    Ent_password.delete(0, 'end')


def p_on_leave(event):
    password = Ent_password.get()
    if password == '':
        Ent_password.insert(0, 'Password')


def cp_on_enter(event):
    Ent_confirm_password.delete(0, 'end')


def cp_on_leave(event):
    conf_password = Ent_confirm_password.get()
    if conf_password == '':
        Ent_confirm_password.insert(0, 'Confirm Password')


def n_on_enter(event):
    Ent_name.delete(0, 'end')


def n_on_leave(event):
    name = Ent_name.get()
    if name == '':
        Ent_name.insert(0, 'Name')


def sk_on_enter(event):
    Ent_security_key.delete(0, 'end')


def sk_on_leave(event):
    security_key = Ent_security_key.get()
    if security_key == '':
        Ent_security_key.insert(0, "What is your first pet's name")


def signup():
    print('This signed you up')
    DIC_username.append(Ent_username.get())
    DIC_password.append(Ent_password.get())
    print(Ent_email.get())
    print(Ent_username.get())
    print(Ent_password.get())
    print(Ent_confirm_password.get())
    print(Ent_name.get())
    print(Ent_security_key.get())
    signup_root.destroy()
    if var.get() == 0:
        messagebox.showerror('Invalid', 'Terms and Conditions not agreed')
    else:
        import Login_page


def ald_acc():
    print("Already have an account")
    import Login_page


# ----------------------------------------------------------------------------------------------------------------------
# Widgets

frm_1 = Frame(signup_root)
frm_1.place(x=120, y=120)

image = Image.open('rndm_image.jpg')
image = ImageTk.PhotoImage(image)  # PIL solution
Lbl_logo = Label(frm_1, image=image, activebackground='white')
Lbl_logo.pack()

signup_frame = Frame(signup_root, width=375, height=450, bg='white')
signup_frame.place(x=480, y=30)

signup_heading = Label(signup_frame, text="Sign in", fg="#57a1f8", bg="white",
                       font=('Microsoft Yahei UI Light', 23, 'bold'))
signup_heading.place(x=115, y=5)

Ent_email = Entry(signup_frame, width=30, fg='black', bg='white', bd=0)
Ent_email.place(x=70, y=80)
Ent_email.insert(0, 'Email Address')
Ent_email.bind('<FocusIn>', e_on_enter)
Ent_email.bind('<FocusOut>', e_on_leave)
Frame(signup_frame, width=200, height=2, bg='black').place(x=70, y=100)

Ent_username = Entry(signup_frame, width=25, fg='black', bg='white', bd=0)
Ent_username.place(x=70, y=120)
Ent_username.insert(0, 'Username')
Ent_username.bind('<FocusIn>', u_on_enter)
Ent_username.bind('<FocusOut>', u_on_leave)
Frame(signup_frame, width=200, height=2, bg='black').place(x=70, y=140)

Ent_password = Entry(signup_frame, width=25, fg='black', bg='white', bd=0)
Ent_password.place(x=70, y=160)
Ent_password.insert(0, 'Password')
Ent_password.bind('<FocusIn>', p_on_enter)
Ent_password.bind('<FocusOut>', p_on_leave)
Frame(signup_frame, width=200, height=2, bg='black').place(x=70, y=180)

Ent_confirm_password = Entry(signup_frame, width=25, fg='black', bg='white', bd=0)
Ent_confirm_password.place(x=70, y=200)
Ent_confirm_password.insert(0, 'Confirm Password')
Ent_confirm_password.bind('<FocusIn>', cp_on_enter)
Ent_confirm_password.bind('<FocusOut>', cp_on_leave)
Frame(signup_frame, width=200, height=2, bg='black').place(x=70, y=220)

Ent_name = Entry(signup_frame, width=25, fg='black', bg='white', bd=0)
Ent_name.place(x=70, y=240)
Ent_name.insert(0, 'Name')
Ent_name.bind('<FocusIn>', n_on_enter)
Ent_name.bind('<FocusOut>', n_on_leave)
Frame(signup_frame, width=200, height=2, bg='black').place(x=70, y=260)

Ent_security_key = Entry(signup_frame, width=30, fg='black', bg='white', bd=0)
Ent_security_key.place(x=70, y=280)
Ent_security_key.insert(0, "What was your first pet's name?")
Ent_security_key.bind('<FocusIn>', sk_on_enter)
Ent_security_key.bind('<FocusOut>', sk_on_leave)
Frame(signup_frame, width=200, height=2, bg='black').place(x=70, y=300)

Chkbox_terms_conditions = Checkbutton(signup_frame, text='I agree to the Terms and Conditions',
                                      fg='black', bg='white', activebackground='white', variable=var)
Chkbox_terms_conditions.place(x=70, y=315)

Btn_signup = Button(signup_frame, text='Sign Up', fg='black', bg='white', bd=5, activebackground='white',
                    font=16, cursor='heart', command=signup)
Btn_signup.place(x=130, y=345)

Btn_already_acc = sign_up = Button(signup_frame, width=20, text='Already have an account', border=0, bg='white',
                                   cursor='hand2', fg='#57a1f8', command=ald_acc)
Btn_already_acc.place(x=230, y=420)

# ----------------------------------------------------------------------------------------------------------------------
# Probe


# ----------------------------------------------------------------------------------------------------------------------
# Main-loops

signup_root.mainloop()

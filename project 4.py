from tkinter import *
from tkinter import ttk  # here ttk is module of tkinter package
from tkinter import messagebox

win = Tk()
win.resizable(width=False, height=False)
win.state('zoomed')
bgclr = '#00ff80'
win.configure(bg=bgclr)
title = Label(win, text='Bank Automation', font=('', 50, 'bold'), fg='black', bg=bgclr)
title.pack()


def homescreen(prvfrm=None):
    if (prvfrm != None):
        prvfrm.destroy()
    frm = Frame(win, bg='yellow')
    frm.place(x=0, y=100, relwidth=1, relheight=1)
    user_lbl = Label(frm, text='Username:', font=('', 20, ''), fg='blue', bg='yellow')
    user_lbl.place(x=400, y=100)

    pass_lbl = Label(frm, text='Password:', font=('', 20, ''), fg='blue', bg='yellow')
    pass_lbl.place(x=400, y=150)

    type_lbl = Label(frm, text='User type:', font=('', 20, ''), fg='blue', bg='yellow')
    type_lbl.place(x=400, y=200)

    user_entry = Entry(frm, bg='powder blue', bd=5, width=15, font=('', 15, ''))
    user_entry.place(x=580, y=100)
    user_entry.focus()

    pass_entry = Entry(frm, show='*', bg='powder blue', bd=5, width=15, font=('', 15, ''))
    pass_entry.place(x=580, y=150)

    type_dropdown = ttk.Combobox(frm, values=['User', 'Admin'], font=('', 11, ''))
    type_dropdown.current(0)
    type_dropdown.place(x=580, y=200)

    login_btn = Button(frm, text='login', command=lambda: validatehomescreen(user_entry, pass_entry, type_dropdown),
                       width=10, font=('', 12, ''), bg='powder blue', bd=5)
    login_btn.place(x=400, y=300)

    reset_btn = Button(frm, text='reset', command=lambda: resethome(user_entry, pass_entry), width=10,
                       font=('', 12, ''), bg='powder blue', bd=5)
    reset_btn.place(x=550, y=300)

    newuser_btn = Button(frm, text='New User', command=lambda: newuserscreen(frm), width=10, font=('', 12, ''),
                         bg='powder blue', bd=5)
    newuser_btn.place(x=700, y=300)

    fp_btn = Button(frm, text='Forgot password', command=lambda: forgotpassscreen(frm), width=25, font=('', 12, ''),
                    bg='powder blue', bd=5)
    fp_btn.place(x=500, y=400)


def forgotpassscreen(prvfrm):
    prvfrm.destroy()
    frm = Frame(win, bg='yellow')
    frm.place(x=0, y=100, relwidth=1, relheight=1)
    user_lbl = Label(frm, text='Username:', font=('', 20, ''), fg='blue', bg='yellow')
    user_lbl.place(x=400, y=100)

    email_lbl = Label(frm, text='Email:', font=('', 20, ''), fg='blue', bg='yellow')
    email_lbl.place(x=400, y=150)

    mob_lbl = Label(frm, text='Mobile:', font=('', 20, ''), fg='blue', bg='yellow')
    mob_lbl.place(x=400, y=200)

    user_entry = Entry(frm, bg='powder blue', bd=5, width=15, font=('', 15, ''))
    user_entry.place(x=580, y=100)
    user_entry.focus()

    email_entry = Entry(frm, bg='powder blue', bd=5, width=15, font=('', 15, ''))
    email_entry.place(x=580, y=150)

    mob_entry = Entry(frm, bg='powder blue', bd=5, width=15, font=('', 15, ''))
    mob_entry.place(x=580, y=200)

    rcvr_btn = Button(frm, text='Recover',command=lambda: validateforgotpassscreen(user_entry, email_entry, mob_entry), width=10, font=('', 12, ''), bg='powder blue', bd=5)
    rcvr_btn.place(x=500, y=300)

    reset_btn = Button(frm, text='reset', command=lambda: resetforgotpass(user_entry, email_entry, mob_entry), width=10,
                       font=('', 12, ''), bg='powder blue', bd=5)
    reset_btn.place(x=650, y=300)

    back_btn = Button(frm, text='back', command=lambda: homescreen(frm), width=10, font=('', 12, ''), bg='powder blue',
                      bd=5)
    back_btn.place(x=50, y=20)


def newuserscreen(prvfrm):
    prvfrm.destroy()
    frm = Frame(win, bg='yellow')
    frm.place(x=0, y=100, relwidth=1, relheight=1)
    user_lbl = Label(frm, text='Username:', font=('', 20, ''), fg='blue', bg='yellow')
    user_lbl.place(x=400, y=100)

    email_lbl = Label(frm, text='Email:', font=('', 20, ''), fg='blue', bg='yellow')
    email_lbl.place(x=400, y=150)

    mob_lbl = Label(frm, text='Mobile:', font=('', 20, ''), fg='blue', bg='yellow')
    mob_lbl.place(x=400, y=200)

    type_lbl = Label(frm, text='Account type:', font=('', 20, ''), fg='blue', bg='yellow')
    type_lbl.place(x=400, y=250)

    bal_lbl = Label(frm, text='Initial bal:', font=('', 20, ''), fg='blue', bg='yellow')
    bal_lbl.place(x=400, y=300)

    pass_lbl = Label(frm, text='Password:', font=('', 20, ''), fg='blue', bg='yellow')
    pass_lbl.place(x=400, y=350)

    user_entry = Entry(frm, bg='powder blue', bd=5, width=15, font=('', 15, ''))
    user_entry.place(x=580, y=100)
    user_entry.focus()

    email_entry = Entry(frm, bg='powder blue', bd=5, width=15, font=('', 15, ''))
    email_entry.place(x=580, y=150)

    mob_entry = Entry(frm, bg='powder blue', bd=5, width=15, font=('', 15, ''))
    mob_entry.place(x=580, y=200)

    type_dropdown = ttk.Combobox(frm, values=['Saving', 'Current'], font=('', 11, ''))
    type_dropdown.current(0)
    type_dropdown.place(x=580, y=253)

    bal_entry = Entry(frm, bg='powder blue', bd=5, width=15, font=('', 15, ''))
    bal_entry.place(x=580, y=300)

    pass_entry = Entry(frm, bg='powder blue', bd=5, width=15, font=('', 15, ''))
    pass_entry.place(x=580, y=350)

    open_btn = Button(frm, text='Open Account', width=15, font=('', 12, ''), bg='powder blue', bd=5)
    open_btn.place(x=480, y=450)

    reset_btn = Button(frm, text='reset',
                       command=lambda: resetnewuser(user_entry, pass_entry, mob_entry, email_entry, type_dropdown,
                                                    bal_entry), width=15, font=('', 12, ''), bg='powder blue', bd=5)
    reset_btn.place(x=670, y=450)

    back_btn = Button(frm, text='back', command=lambda: homescreen(), width=10, font=('', 12, ''), bg='powder blue',
                      bd=5)
    back_btn.place(x=50, y=20)


def resethome(eu, ep):
    eu.delete(0, END)
    ep.delete(0, END)
    eu.focus()


def resetnewuser(eu, ep, em, ee, et, eb):
    eu.delete(0, END)
    ep.delete(0, END)
    em.delete(0, END)
    ee.delete(0, END)
    et.current(0)
    eb.delete(0, END)
    eu.focus()


def resetforgotpass(eu, em, ee):
    eu.delete(0, END)
    em.delete(0, END)
    ee.delete(0, END)
    eu.focus()


def validatehomescreen(eu, ep, et):
    u = eu.get()
    p = ep.get()
    t = et.get()
    if (len(u) == 0 or len(p) == 0):
        messagebox.showwarning('Validation Failed', "Username/Password can't be empty")
        return
    else:
        if (u == 'abc' and p == 'abc' and t == 'User'):
            messagebox.showinfo('Login Success', "Welcome..")
        else:
            messagebox.showerror('Login Failed', "Invalid Username/Password")
def validateforgotpassscreen(eu, ee, em):
    u = eu.get()
    e = ee.get()
    m = em.get()
    if (len(u) == 0 or len(e) == 0 or len(m)==0):
        messagebox.showwarning('Validation Failed', "coloum can't be empty")
        return
    else:
        if u == 'abc' and e == 'abc' and  m == '123':
            messagebox.showinfo('recover Success', "password change..")
        else:
            messagebox.showerror('recover Failed', "Invalid coloum")



homescreen()
win.mainloop()

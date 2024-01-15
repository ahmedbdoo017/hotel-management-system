from tkinter import *
import tkinter.messagebox as tmsg
import Admin
import resption 
from style import *
import sqlite3
from PIL import Image, ImageTk


conn = sqlite3.connect('hotel.db')
cur = conn.cursor()

cur.execute('select * from Admins')
rs = cur.fetchall()
user_ad = rs[0][0]
pass_ad = rs[0][1]
user_re = rs[1][0]
pass_re = rs[1][1]

conn.close()

def login():
    root = Tk()
    img(root)
    def submit():
        user = uservalue.get()
        passw = passvalue.get()
        
            

        if user == user_ad and passw == pass_ad:
           # sarv = "1"
            to_admin(root)

        elif user == user_re and passw == pass_re:
            to_resption(root)

        else:
            tmsg.showinfo("WRONG INPUT", "Invalid Username or Password")
           

    root.title("Login Window")
    root.geometry("400x200+500+250")
    root.config(bg = dark_blue)
    root.resizable(0, 0)


    Label(root, text="Username", font=font, bg=dark_blue,fg=white).place(x=50,y=50)
    Label(root, text="Password", font=font, bg=dark_blue,fg=white).place(x=50,y=80)

    uservalue = StringVar()
    passvalue = StringVar()

    userentry = Entry(root, textvariable=uservalue).place(x=120,y=50)
    passentry = Entry(root, textvariable=passvalue, show="*").place(x=120,y=80)


    Button(root, text="LOGIN", font=font, bg=dark_blue, fg=white, relief=relife, command=submit).place(x=70,y=120)
    Button(root, text="CLOSE", font=font, bg=dark_blue, fg=white, relief=relife, command=root.destroy).place(x=150,y=120)
    root.mainloop()

    
def to_resption(root):
    root.destroy()
    new_win = Tk()
    resption.Recep(new_win)
    
def to_admin(root):
    root.destroy()
    new_win = Tk()
    Admin.admin(new_win)

def img(self, root=None):
    self.bg = PhotoImage(file="1.png")
    Label(root, image=self.bg,bg=dark_blue).place(x=250, y=30)
    



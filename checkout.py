import datetime
from PIL import Image, ImageTk
from tkinter import *
from tkinter.ttk import * 
import tkinter.messagebox as tmsg
import resption
import sqlite3
from style import *


def checkout(root):
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute("select customer_id from Customers")
    c_id = cur.fetchall()
    conn.close()
    
    
    img(self=root)
    root.geometry("1110x500+300+120")
    root.config(bg = black)   
    #root.config(bg="WHITE")
    root.resizable(0,0)
    
    
    info = []
    
    def check():
        c = [int(cust_ID.get())]
        print(c,type(c))
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        cur.execute("select * from Customers where customer_id = ?", c)
        c_info = cur.fetchall()
        for i in c_info:
            info.append(i)
            
        print(c_info)
        conn.close()
        
        Label(root, text=str(c_info[0][1]),background=white, width=15, anchor=W).place(x=230, y=140)
        Label(root, text=str(c_info[0][6]),background=white, width=15, anchor=W).place(x=230, y=210)
        Label(root, text=str(c_info[0][5]),background=white, width=15, anchor=W).place(x=230, y=280)
        ch_value = datetime.datetime.now()
        Label(root, text=f"{ch_value}", width=15,background=white).place(x=230, y=340)    
    
    def out():
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        cur.execute('delete from Customers where customer_id = ?', [info[0][0]])
        cur.execute("update Rooms set availability = 'available' where room_num = ? ", [info[0][6]])
        conn.commit()
        conn.close()
        tmsg.showinfo("Info", "successful checkout")
        
    
    Customer_ID = Label(root,text='Customer ID:',font= ('Tahoma', 15 ),foreground="#F0B86E",background=black).place(x=30, y=77)
    cust_ID = StringVar()
    Combobox_ID = Combobox(root, state='readonly', textvariable=cust_ID, values=c_id, width=25).place(x=230, y=80)
    Name = Label(root, text="Name: ",foreground="#F0B86E",background=black, width=15, font=('Tahoma', 15 )).place(x=30,y=140)
    Room_Number = Label(root, text="Room Number: ",foreground="#F0B86E",background=black, width=15,font=('Tahoma', 15 )).place(x=30, y=210)
    Checkin_Time = Label(root, text="Checkin Time: ",foreground="#F0B86E",background=black,  font=('Tahoma', 15 )).place(x=30, y=280)
    Checkout_Time = Label(root, text="Checkout Time: ",foreground="#F0B86E",background=black, width=15, font=('Tahoma', 15 )).place(x=30, y=340)
    Checkout = Button(root, text="Checkout" ,  width=15 , command=out).place(x=150, y=400)
    Back = Button(root, text="Back",  width=15, command=lambda:to_resption(root)).place(x=20, y=400)
    Check = Button(root, text="Check",  width=15, command=check).place(x=280, y=400)
    
    
def img(self, root=None):
        self.bg = PhotoImage(file="8.PNG")
        Label(root, image=self.bg, width=550).place(x=420, y=20)

      
def to_resption(root):
    root.destroy()
    new_win = Tk()
    resption.Recep(new_win)    

def call():
    root = Tk()
    checkout(root)
    root.mainloop()
#call()    
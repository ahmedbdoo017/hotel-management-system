import datetime
from tkinter import *
from tkinter.ttk import * 
import tkinter.messagebox as tmsg
import resption
import sqlite3
from style import *
from PIL import Image, ImageTk





def update(root):
    img(root)
  
    info = []
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute("select customer_id from Customers")
    c_id = cur.fetchall()
    conn.close()
    
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute("select room_num from Rooms where availability = 'available'")
    room_ava = cur.fetchall()
    conn.close()
    
    
    def check():
        cid = int(cust_ID.get())
        c = [cid]
        print(c,type(c))
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        cur.execute("select * from Customers where customer_id = ?", c)
        c_info = cur.fetchall()
        for i in c_info:
            info.append(i)
          
        print(c_info)
        Label(root, text=str(c_info[0][6]), width=15, anchor=W).place(x=230, y=140)
        Label(root, text=str(c_info[0][1]), width=15, anchor=W).place(x=230, y=210)
        Label(root, text=str(c_info[0][5]), width=15, anchor=W).place(x=230, y=280)
        Label(root, text=str(c_info[0][4]), width=15, anchor=W).place(x=230, y=350)
        conn.close()
       
  
   
    root.title('Check in')
    root.geometry("950x500+300+120")
    root.config(bg=black)
    root.resizable(0,0)
    cust_ID = StringVar()
    Combobox_ID = Combobox(root, state='readonly',foreground="#F0B86E",background=black, textvariable=cust_ID, values=c_id, width=25).place(x=230, y=60)
    Customer_ID =Label(root, text="Customer ID  ",foreground="#F0B86E",background=black ,width=15, font=('Tahoma', 15 )).place(x=50, y=60)
    Room_Number = Label(root, text="Room Number ",foreground="#F0B86E",background=black , width=15, font=('Tahoma', 15 )).place(x=50, y=110)
    name=StringVar()
    Name =Label(root, text="Name ",foreground="#F0B86E",background=black,textvariable= name.get(), width=15, font=('Tahoma', 15 )).place(x=50, y=170)

    Checkin_Time = Label(root, text="Checkin Time",foreground="#F0B86E",background=black, width=15, font=('Tahoma', 15 )).place(x=50, y=240)

    Amount_Paid = Label(root, text="Amount Paid ",foreground="#F0B86E",background=black, width=15, font=('Tahoma', 15 )).place(x=50, y=310)
    
    
    Check = Button(root, text="Check", command=check ,width=15,).place(x=50, y=430)
    Update = Button(root, text="Update", command = lambda : up(),width=15, ).place(x=180, y=430)
    Back = Button(root, text="Back", command=lambda:to_resption(root) , width=15).place(x=310, y=430)
    
    def up():
        
       def update1():
            #print(room_value.get())
            room = room_value.get()
            name = name_value.get()
            deposit = amount_value.get()
            conn = sqlite3.connect('hotel.db')
            cur = conn.cursor()
            print(name,room,deposit,info[0][4], info[0][0])
            cur.execute("UPDATE Customers SET name = ?,room_num = ?,deposit = ? WHERE customer_id = ?", (name, room, deposit+info[0][4], info[0][0]))
            cur.execute("update Rooms set availability = 'occupied' where room_num = ? ", [room])
            conn.commit()
            conn.close()
            tmsg.showinfo("Info", "successful update")
            
       conn = sqlite3.connect('hotel.db')
       cur = conn.cursor()
       cur.execute("update Rooms set availability = 'available' where room_num = ? ", ([info[0][6]]))
       conn.commit()
       conn.close()
        
       print(info)
       print(room_ava)
       root2 = Tk()
       root2.title("Update Data")
       root2.geometry("250x500+50+120")
       root2.config(bg=black)
       root2.resizable(0,0)
       
       Label(root2, text="Enter valid data in each field",foreground="#F0B86E",background=black ).place(x=50, y=20)
       cust_ID2 = Label(root2, text=cust_ID.get(),font=font,foreground=black).place(x=50, y=50)
       
       room_value = IntVar(root2)
       #room_ava.append(info[0][6])
       room_num = Combobox(root2, state='readonly', textvariable=room_value, values=room_ava,width=25).place(x=50, y=110)
       
       name_value = StringVar(root2)
       Name2 = Entry(root2, textvariable=name_value, width=25).place(x=50,y=150)
       
       Label(root2, text = str(info[0][5]),font=font,foreground=black).place(x=50, y=240)
       
       amount_value = IntVar(root2)
       amount_entry = Entry(root2, textvariable=amount_value, width=25).place(x=50, y=310)
       
       Button(root2, text="Update", width=15, command=lambda: update1()).place(x=80,y=430)

    
       

def to_resption(root):
    root.destroy()
    new_win = Tk()
    resption.Recep(new_win)
    
def img(self, root=None):
    self.bg = PhotoImage(file="f.png")
    Label(root, image=self.bg, width=500).place(x=500, y=60)
def call():
    root = Tk()
    update(root)
    root.mainloop()
    
#call()   






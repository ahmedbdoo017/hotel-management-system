import tkinter.ttk
from datetime import datetime
from tkinter import *
import resption
import sqlite3
from style import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg


def customer(root):
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute("select room_num from Rooms where availability = 'available'")
    room_ava = cur.fetchall()
    conn.close()
    
    root.title("ADD New Customer Form")
    root.geometry("850x470+300+120")
    root.resizable(0, 0)
    root.config(bg = black)
    img(root)

    def ADD():
        customer_id = ID_value.get()
        name = name_value.get()
        gender = g_value.get()
        country = c_value.get()
        room = rn_value.get()
        checkintime = ch_value
        deposit = d_value.get()
        #checkin_time = ch_value
        
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        cur.execute("Insert into Customers(customer_id, name, gender, country, deposit, checkin_time, room_num) values(?,?,?,?,?,?,?)",
                    (int(customer_id), name, gender, country, int(deposit), f"{checkintime}", int(room)))
        # q = "insert into employee(name,age,gender,job,salary,phone,email) values(%s,%s,%s,%s,%s,%s,%s)"
        # v = (name,age,gender,job,salary,phone,email1)
        # Conn.mydb.commit()
        cur.execute(
            "update Rooms set availability = 'occupied' where room_num = ? ", (room))
        conn.commit()
        conn.close()
        tmsg.showinfo("Info", "successful checkin")

    head = Label(root, text="Add New Customer Form", borderwidth=1, width=30,
                 relief=SUNKEN,bg="#F0B86E", fg='black').place(x=30, y=20)
    Customer_ID = Label(root, text="Customer ID : ",
                        borderwidth=1, width=15, relief=FLAT,bg="#F0B86E").place(x=30, y=70)
    Name = Label(root, text="Name : ", borderwidth=1,bg="#F0B86E",
                 width=15, relief=FLAT).place(x=30, y=120)
    Gender = Label(root, text="Gender : ", borderwidth=1,
                   width=15, relief=FLAT,bg="#F0B86E").place(x=30, y=170)
    Country = Label(root, text="Country : ", borderwidth=1,
                    width=15, relief=FLAT,bg="#F0B86E").place(x=30, y=220)
    Room_Number = Label(root, text="Room Number : ",
                        borderwidth=1, width=15, relief=FLAT,bg="#F0B86E").place(x=30, y=270)
    Checkin_Time = Label(root, text="Checkin Time : ",
                         borderwidth=1, width=15, relief=FLAT,bg="#F0B86E").place(x=30, y=320)
    Deposit = Label(root, text="Deposit : ", borderwidth=1,
                    width=15, relief=FLAT,bg="#F0B86E").place(x=30, y=370)

    ID_value = StringVar()
    ID_entry = Entry(root, textvariable=ID_value).place(x=170, y=70)

    name_value = StringVar()
    name_entry = Entry(root, textvariable=name_value).place(x=170, y=120)

    g_value = StringVar()
    g_value.set('M')
    M = Radiobutton(root, text="MALE",bg=black,fg="#F0B86E", padx=14, value='M',
                    variable=g_value).place(x=150, y=170)
    F = Radiobutton(root, text="FEMALE",bg=black,fg="#F0B86E", padx=14, value='F',
                    variable=g_value).place(x=220, y=170)

    c_value = StringVar()
    c_entry = Entry(root, textvariable=c_value).place(x=170, y=220)
    
    rn_value = StringVar()
    print(room_ava)
    tkinter.ttk.Combobox(root, state='readonly', textvariable=rn_value,
                         values=room_ava, width=20).place(x=170, y=270)

    ch_value = datetime.now()
    Label(root, text=f"{ch_value}",background=white).place(x=170, y=320)

    d_value = StringVar()
    d_entry = Entry(root, textvariable=d_value).place(x=170, y=370)

    Button(root, text="ADD",bg="#F0B86E", command=lambda: ADD()).place(x=100, y=420)
    Button(root, text="BACK", bg="#F0B86E",command=lambda: to_resption(
        root)).place(x=170, y=420)


def to_resption(root):
    root.destroy()
    new_win = Tk()
    resption.Recep(new_win)

   
def img(self, new_win10=None):
    self.bg = PhotoImage(file="cus.png")
    Label(new_win10, image=self.bg, width=506 , height=300,bg=black).place(x=350, y=55)
def call():
    root = Tk()
    customer(root)
    root.mainloop()


#call()
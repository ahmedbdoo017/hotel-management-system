from tkinter import *
import tkinter.ttk
import Admin
import tkinter.messagebox as tmsg
import sqlite3
from style import *


def Addroom(root):
    
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    
    cur.execute("select room_num from Rooms")
    num = cur.fetchall()
    #print((num[0][0]))
    print(num)
    conn.close()

    def submit():
        room_num = room_value.get()
        price = price_value.get()
        bed_type = bed_value.get()
        print(int(price))
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        cur.execute("insert into Rooms(price,bed_type,availability)values(?,?,'available')",(int(price),bed_type))
        conn.commit()
        conn.close()
        tmsg.showinfo("Info", "successful add")
        

    root.title("Add Room")
    root.geometry("550x270+350+200")
    root.resizable(0, 0)
    root.config(bg = harrdy)    
    Label(root, text="Room Number : ", borderwidth=1, width=15,bg=harrdy,fg=dark_blue).place(x=30, y=40)
    Price = Label(root, text="Price : ", borderwidth=1, width=15,bg=harrdy,fg=dark_blue).place(x=30, y=90)
    Bed_Type = Label(root, text="Bed Type : ", borderwidth=1, width=15,bg=harrdy,fg=dark_blue).place(x=30, y=140)

    room_value = StringVar()
    price_value = StringVar()
    bed_value = StringVar()
    #bed_value.set('Single')
    room_value.set(value=str(len(num)+1))
    room_lbl = Label(root, textvariable=room_value).place(x=170, y=40, width=245)
    price_en = Entry(root, textvariable=price_value).place(x=170, y=90, width=245)

    tkinter.ttk.Combobox(root, state='readonly', textvariable=bed_value, values=['Single','Double']).place(x=170, y=140,width=245)

    Button(root, text="SUBMIT", command=submit,bg="#EADBC8").place(x=200, y=190)
    Button(root, text="CANCEL",command=lambda: to_admin(root),bg="#EADBC8").place(x=270, y=190)
    
def to_admin(root):
    root.destroy()
    new_win = Tk()
    Admin.admin(new_win)

def call():
    root = Tk()
    Addroom(root)
    root.mainloop()

#call()


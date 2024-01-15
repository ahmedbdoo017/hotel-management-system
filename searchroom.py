from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import ttk
import resption
from style import *
import sqlite3

def room(root):
    
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute('select * from Rooms')
    rooms = cur.fetchall()
    conn.close()
    
    
    def search():
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        ex = ''
        val = search_value.get()
        for item in tree.get_children():
            tree.delete(item)
        s = comb_value.get()
        if s == 'Availability':
            ex = 'select * from Rooms where availability like ? '
            val = '%'+val+'%'
        elif s == 'Bed Type':
            ex = 'select * from Rooms where bed_type like ? '
            val = '%'+val+'%'
        elif s == 'Room Number':
            ex = 'select * from Rooms where room_num = ? '
            val = int(val)
        else :
            ex = 'select * from Rooms where price <= ?'
            val = int(val)
        try:
            cur.execute(ex,[val])
            res = cur.fetchall()
            for room in res:
                tree.insert(parent='', index='end', values=room, iid=str(room[0]))
            
        except:
            
            tmsg.showerror("WRONG INPUT", "Invalid search")
        print(ex,val)
        conn.close()
        
    
    
    root.title("Search Room")
    root.geometry("935x500+300+120")
    root.config(bg = black)
    root.resizable(0,0)
    cols = ('Room number', 'Price', 'Bedtype', 'Availability')
    tree = ttk.Treeview(root, columns=cols, show='headings',height= 15)
    for col in cols:
        tree.heading(col, text=col)

        tree.column("Room number", width=220, anchor=CENTER)
        tree.column("Price", width=250, anchor=CENTER)
        tree.column("Bedtype", width=220, anchor=CENTER)
        tree.column("Availability", width=220, anchor=CENTER)
        tree.place(x=10, y=20)

    for room in rooms:
        tree.insert(parent='', index='end', values=room, iid=str(room[0]))
    '''
    scrollbar = Scrollbar(root, orient='vertical', command=tree.yview())
    tree.configure(yscroll=scrollbar.set)
    tree.grid(row=0, column=0)
    scrollbar.grid(row=0, column=1, sticky='ns')
    '''


    Button(root, text="Back",foreground=black,background="#F0B86E", command=lambda:to_resption(root)).place(x=400, y=420)
    Button(root, text="Show Selections",foreground=black,background="#F0B86E", command=search).place(x=450, y=420)

    search_value = StringVar()
    search_box = Entry(root,textvariable=search_value)
    Label(root, text="Search : ",foreground="#F0B86E",background=black, borderwidth=1, width=15, relief=SUNKEN).place(x=50, y=370)
    search_box.grid(row=0, columns=1, padx=170,pady=370)

    comb_value = StringVar()
    drop = ttk.Combobox(root, state='readonly', textvariable=comb_value, values= ["Availability", "Bed Type","Price","Room Number"])
    drop.current(0)
    drop.grid(row=0,column=1 ,padx=250,pady=370 )

def to_resption(root):
    root.destroy()
    new_win = Tk()
    resption.Recep(new_win)

def call():
    root = Tk()
    room(root)
    root.mainloop()

#call()
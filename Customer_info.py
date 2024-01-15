# import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
import resption
from style import *
import sqlite3


def info(root):
    
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute('select * from Customers')
    res = cur.fetchall()
    conn.close()
    
    root.title("Customer Info")
    root.geometry("955x400+300+120")
    root.config(bg = black)
    root.resizable(0,0)
    cols = ( 'Customer ID', 'Name', 'Gender', 'Country', 'Deposit', 'Checkin Time', 'Room')
    tree = ttk.Treeview(root, columns=cols, show='headings', height=14)
    for col in cols:
        tree.heading(col, text=col)
       
        tree.column("Customer ID", width=130, anchor=CENTER)
        tree.column("Name", width=130, anchor=CENTER)
        tree.column("Gender", width=130, anchor=CENTER)
        tree.column("Country", width=130, anchor=CENTER)
        tree.column("Room", width=130, anchor=CENTER)
        tree.column("Deposit", width=130, anchor=CENTER)
        tree.column("Checkin Time", width=155, anchor=CENTER)
        tree.place(x=10, y=20)
        
    for cust in res:
        tree.insert(parent='', index='end', values=cust, iid=str(cust[0]))
    '''    
    scrollbar = Scrollbar(root, orient='vertical', command=tree.yview())
    tree.configure(yscrollcommand=scrollbar.set)
    tree.grid(row=0, column=0)
    scrollbar.grid(row=0, column=1, sticky='ns')
    '''

    Button(root, text="Back", width=10,bg="#F0B86E", command=lambda:to_resption(root)).place(x=450, y=350)

def to_resption(root):
    root.destroy()
    new_win = Tk()
    resption.Recep(new_win)
        
def call():
    root = Tk()
    info(root)
    root.mainloop()

#call()



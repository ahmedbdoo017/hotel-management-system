from tkinter import ttk,messagebox
from tkinter import *
import resption
from style import *
import sqlite3
def emp(root):
    
    
    conn = sqlite3.connect('hotel.db')
    cur = conn.cursor()
    cur.execute('select * from Employees')
    employees = cur.fetchall()
    conn.close()
    # root = Tk()
    root.geometry("750x450+300+120")
    root.title("Employee info")
    root.config(bg = black)
    root.resizable(0,0)
    cols = ('id','ssn', 'name', 'age', 'gender', 'job', 'phone', 'salary')
    tree = ttk.Treeview(root, columns=cols, show='headings', height=14)
    for col in cols:
        tree.heading(col, text=col)
        tree.column("id", width=10, anchor=CENTER)
        tree.column("name", width=100, anchor=CENTER)
        tree.column("age", width=80, anchor=CENTER)
        tree.column("gender", width=100, anchor=CENTER)
        tree.column("job", width=90, anchor=CENTER)
        tree.column("salary", width=90, anchor=CENTER)
        tree.column("phone", width=110, anchor=CENTER)
        tree.column("ssn", width=150, anchor=CENTER)
        tree.place(x=10, y=20)
    
    for employee in employees:
        tree.insert(parent='', index='end', values=employee, iid=str(employee[0]))
    '''  
    scrollbar = Scrollbar(root, orient='vertical', command=tree.yview())
    tree.configure(yscrollcommand=scrollbar.set)
    tree.grid(row=0, column=0)
    scrollbar.grid(row=0, column=1, sticky='ns')
    '''


    Button(root, text="BACK",bg="#F0B86E", command=lambda:to_resption(root)).place(x=350, y=400)

def to_resption(root):
    root.destroy()
    new_win = Tk()
    resption.Recep(new_win)

def call():
    root = Tk()
    emp(root)
    root.mainloop()

#call()
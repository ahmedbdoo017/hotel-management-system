import tkinter.ttk
from tkinter import *
import tkinter.messagebox as tmsg
import Admin 
import sqlite3
from style import *

def addemp(root):

    def submit():
        name = name_value.get()
        age = age_value.get()
        gender = gender_value.get()
        job = job_value.get()
        salary = salary_value.get()
        phone = phone_value.get()
        ssn = ssn_value.get()
        conn = sqlite3.connect('hotel.db')
        cur = conn.cursor()
        cur.execute("insert into Employees(name,age,gender,job,salary,phone_num,ssn)values(?,?,?,?,?,?,?)",(name,age,gender,job,salary,phone,ssn))
        conn.commit()
        conn.close()
        tmsg.showinfo("Info", "successful add")
        
        

    root.title("Add Employee")
    root.geometry("350x470+300+120")
    root.resizable(0, 0)
    root.config(bg = harrdy)
    
    def to_admin(root):
        root.destroy()
        new_win = Tk()
        Admin.admin(new_win)
    
    Label(root, text="Name : ", borderwidth=1, width=15,bg=harrdy,fg=dark_blue).place(x=30, y=70)
    Label(root, text="Age : ", borderwidth=1, width=15,bg=harrdy,fg=dark_blue).place(x=30, y=120)
    Label(root, text="Gender : ", borderwidth=1, width=15,bg=harrdy,fg=dark_blue).place(x=30, y=170)
    Label(root, text="Job : ", borderwidth=1, width=15,bg=harrdy,fg=dark_blue).place(x=30, y=220)
    Label(root, text="Salary : ", borderwidth=1, width=15,bg=harrdy,fg=dark_blue).place(x=30, y=270)
    Label(root, text="Phone : ", borderwidth=1, width=15,bg=harrdy,fg=dark_blue).place(x=30, y=320)
    Label(root, text="SSN : ", borderwidth=1, width=15,bg=harrdy,fg=dark_blue).place(x=30, y=370)

    name_value = StringVar()
    name_entry = Entry(root, textvariable=name_value).place(x=170, y=70,width=140)
    

    age_value = StringVar()
    age_entry = Entry(root, textvariable=age_value).place(x=170, y=120,width=140)
    

    gender_value = StringVar()
    Radiobutton(root, text="MALE", padx=14, variable=gender_value, value="Male",bg=harrdy,fg=dark_blue).place(x=150, y=170)
    Radiobutton(root, text="FEMALE", padx=14, variable=gender_value, value="Female",bg=harrdy,fg=dark_blue).place(x=220, y=170)
    

    job_value = StringVar()
    tkinter.ttk.Combobox(root, state='readonly', textvariable=job_value, values=['Front Desk Clerks','Porters','House Keeping','Kitchen Staff','Waiter','Room Service','Manager']).place(x=170, y=220,width=140)
    

    salary_value = StringVar()
    salary_entry = Entry(root, textvariable=salary_value).place(x=170, y=270,width=140)
    

    phone_value = StringVar()
    phone_entry = Entry(root, textvariable=phone_value).place(x=170, y=320,width=140)
    

    ssn_value = StringVar()
    ssn_entry = Entry(root, textvariable=ssn_value).place(x=170, y=370,width=140)
    

    

    Button(root, text="SUBMIT", command=submit, relief=RIDGE,bg="#EADBC8").place(x= 150, y=420)
    Button(root, text="CANCEL", relief=RIDGE,bg="#EADBC8",command=lambda: to_admin(root)).place(x= 220, y=420)
    
def call():
    root = Tk()
    addemp(root)
    root.mainloop()

#call()

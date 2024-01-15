from tkinter import *
import AddEmployee 
import Addroom
import Login
from style import *
def admin(root):
    
    root.title("ADMIN")
    root.geometry("400x200+500+250")
    root.resizable(0, 0)
    root.config(bg = dark_blue)
    def to_AddEmployee(root):
        root.destroy()
        new_win = Tk()
        AddEmployee.addemp(new_win)
            
    def to_Addroom(root):
        root.destroy()
        new_win = Tk()
        Addroom.Addroom(new_win)
        
    def to_login(root):
        root.destroy()

        Login.login()
    
    
    
    ADD_EMPLOYEES = Button(root, text="ADD EMPLOYEES", borderwidth=1,bg=harrdy, width=20,command=lambda:to_AddEmployee(root)).place(x=50,y=30)
    ADD_ROOMS = Button(root, text="ADD ROOMS", borderwidth=1, width=20,bg=harrdy,command=lambda:to_Addroom(root)).place(x=50,y=70)
    QUIT = Button(root, text="QUIT", borderwidth=1, width=20,bg=harrdy,command=lambda:root.destroy()).place(x=50,y=110)
    BACK = Button(root, text="BACK", borderwidth=1, width=20,bg=harrdy,command=lambda:to_login(root)).place(x=50, y= 150)


def call():
    root = Tk()
    admin(root)
    root.mainloop()

#call()


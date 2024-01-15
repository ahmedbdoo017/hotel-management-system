from tkinter import *
from PIL import Image, ImageTk
import Customer_info 
import Login
import checkin
import checkout
import searchroom
import update
import EmployeeInfo
from style import *
 
def Recep(root):
    root.geometry("1000x550+250+100")
    root.resizable(0, 0)
    root.title("RECEPTION")
    root.config(bg = black)

    img(root)




    Button(text="NEW CUSTOMER FORM",command=lambda:to_checkin(root),bg="#F0B86E").place(x=50, y=40, width=150, height=35)
    Button(text="ALL EMPLOYEES",command=lambda:to_employee_info(root),bg="#F0B86E").place(x=50, y=100, width=150, height=35)
    Button(text="CUSTOMER INFO",command=lambda:to_Customer_info(root),bg="#F0B86E").place(x=50, y=160, width=150, height=35)
    Button(text="CHECKOUT",command=lambda:to_checkout(root),bg="#F0B86E").place(x=50, y=220, width=150, height=35)
    Button(text="UPDATE STATUS",command=lambda:to_update(root),bg="#F0B86E").place(x=50, y=280, width=150, height=35)
    Button(text="SEARCH ROOMS",command=lambda:to_searchroom(root),bg="#F0B86E").place(x=50, y=340, width=150, height=35)
    Button(text="LOGOUT",command=lambda:to_login(root),bg="#F0B86E").place(x=50, y=400, width=150, height=35)
    
def img(self, root=NONE):
  self.image = Image.open("DESK.jpg")
  self.photo2 = ImageTk.PhotoImage(self.image)
  label3 = Label(image=self.photo2, height=450, width=700)
  label3.place(x=250, y=40)

def to_login(root):
        root.destroy()
        Login.login()
     
def to_checkin(root):
        root.destroy()
        new_win = Tk()
        checkin.customer(new_win)
    
def to_checkout(root):
        root.destroy()
        new_win = Tk()
        checkout.checkout(new_win)

def to_update(root):
        root.destroy()
        new_win = Tk()
        update.update(new_win)
    
    
def to_Customer_info(root):
        root.destroy()
        new_win = Tk()
        Customer_info.info(new_win)
    
def to_searchroom(root):
        root.destroy()
        new_win = Tk()
        searchroom.room(new_win)
        
def to_employee_info(root):
        root.destroy()
        new_win = Tk()
        EmployeeInfo.emp(new_win)




def call():
    root = Tk()
    Recep(root)
    root.mainloop()
#call()
from openpyxl import *
from tkinter import *
from PIL import ImageTk, Image
import sqlite3


def focus1(event): 

    LastName_field.focus_set() 

def focus2(event): 
 
    FName_field.focus_set() 
  
  

def focus3(event): 
    share_field.focus_set() 
  
   
def focus5(event):
    mobile_no_field.focus_set()
  
  

def focus6(event): 
    email_id_field.focus_set() 
  
      
    
def focus10(event):
    title_field.focus_set()


def clear(): 
    title_field.delete(0, END) 
    LastName_field.delete(0, END) 
    FName_field.delete(0, END) 
    share_field.delete(0, END) 
    mobile_no_field.delete(0, END)
    email_id_field.delete(0, END) 

  
  

    
def insert(): 
    if (title_field.get() == "" and
        LastName_field.get() == "" and
        FName_field.get() == "" and
        share_field.get() == "" and
        mobile_no_field.get() == "" and
        email_id_field.get() == ""): 
              
        print("empty input") 
  
    else: 

        # set focus on the title_field box 
        title_field.focus_set() 
        a=title_field.get()
        b=LastName_field.get()
        c=FName_field.get()
        d=share_field.get()
        f=mobile_no_field.get()
        g=email_id_field.get()
        conn = sqlite3.connect('form3.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Persons (ID TEXT,Last TEXT,First TEXT,Share TEXT,Mobile INT,Email)')
        cursor.execute('INSERT INTO Persons (ID,Last,First,Share,Mobile,Email) VALUES(?,?,?,?,?,?)',(a,b,c,d,f,g,))
        conn.commit()
        clear() 
  
  
if _name_ == "_main_": 
    root = Tk() 
    root.configure(background='white') 
    root.title("Person Info form") 
    root.geometry("800x700") 
    heading = Label(root, text="Form", bg="white") 
    title = Label(root, text="ID", bg="white") 
    LastName = Label(root, text="Last Name", bg="white") 
    FName = Label(root, text="First Name", bg="white") 
    share = Label(root, text="Date of Birth (dd/mm/yyyy)", bg="white") 
    mobile_no = Label(root, text="Mobile No.", bg="white")
    email_id = Label(root, text="Email id", bg="white") 
  
    heading.grid(row=0, column=1) 
    title.grid(row=1, column=0) 
    LastName.grid(row=2, column=0) 
    FName.grid(row=3, column=0) 
    share.grid(row=4, column=0) 
    mobile_no.grid(row=6, column=0)
    email_id.grid(row=7, column=0) 
    
  
    title_field = Entry(root) 
    LastName_field = Entry(root) 
    FName_field = Entry(root) 
    share_field = Entry(root) 
    mobile_no_field = Entry(root)
    email_id_field = Entry(root) 
   
    title_field.bind("<Return>", focus10) 
    LastName_field.bind("<Return>", focus1) 
    FName_field.bind("<Return>", focus1)  
    share_field.bind("<Return>", focus3) 
    mobile_no_field.bind("<Return>", focus5)
    email_id_field.bind("<Return>", focus6) 

    title_field.grid(row=1, column=1, ipadx="50") 
    LastName_field.grid(row=2, column=1, ipadx="50") 
    FName_field.grid(row=3, column=1, ipadx="50") 
    share_field.grid(row=4, column=1, ipadx="50")
    mobile_no_field.grid(row=6, column=1, ipadx="50")
    email_id_field.grid(row=7, column=1, ipadx="50")     

    submit = Button(root, text="Submit", fg="Black", 
                            bg="Red", command=insert) 
    submit.grid(row=29, column=2) 
   
    root.mainloop()
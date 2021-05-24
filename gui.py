 # tkinter
## pyqt
## pygtk
## wxpython
## 
import tkinter
win = tkinter.Tk() # root base window
win.geometry("400x400")
f1 = tkinter.Frame(win)
f2 = tkinter.Frame(win)
#Label
f1.pack()
f2.pack()
l1 = tkinter.Label(f1,text="FirstName " , fg="red")
l1.grid(row =0, column =0 )
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=0, column= 3)
l2 = tkinter.Label(f1,text="LastName ")
l2.grid(row=1, column= 0)
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=1, column= 3)

l3 = tkinter.Label(f2,text="Negotiated" , fg="red")
l3.grid(row=5, column=0)
c1 = tkinter.Checkbutton(f2, text="Deluxe Room Single")
c1.grid(row=6, column=0)
l4 = tkinter.Label(f2, text = "Rs 1700")
l4.grid(row=6, column = 1)
c2 = tkinter.Checkbutton(f2, text="Deluxe Room Double")
c2.grid(row=6, column=2)
l5 = tkinter.Label(f2, text = "Rs 1800")
l5.grid(row=6, column = 3)





win.mainloop()

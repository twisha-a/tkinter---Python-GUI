import tkinter
win = tkinter.Tk()
win.geometry("700x700")
f1 = tkinter.Frame(win)
f2 = tkinter.Frame(win)
f3 = tkinter.Frame(win)
f4 = tkinter.Frame(win)
f5 = tkinter.Frame(win)
#Label
f1.pack()
f2.pack()
f3.pack()
f4.pack()
f5.pack()
l1 = tkinter.Label(f1,text="CAR RENTAL RECEIPT " , font=("Arial", 25, 'bold'))
l1.grid(row =0, column =0 )
#date
l2 = tkinter.Label(f1,text="Date:")
l2.grid(row =1, column =0 )
e1 = tkinter.Entry(f1,width= 10)
e1.grid(row=1, column= 1)
#receipt
l3 = tkinter.Label(f1,text="Receipt#: " )
l3.grid(row =2, column =0 )
e1 = tkinter.Entry(f1,width= 10)
e1.grid(row=2, column= 1)
#rental 
l4 = tkinter.Label(f2,text="Rental Company Info   ", font=('bold' ))
l4.grid(row =3, column =0 )
l4 = tkinter.Label(f2,text="      Lessee Info", font=('bold' ))
l4.grid(row =3, column =2 )

#Company and name
l5 = tkinter.Label(f2,text="Company:" )
l5.grid(row =4, column =0 )
e1 = tkinter.Entry(f2,width= 10)
e1.grid(row=4, column= 1)
l6 = tkinter.Label(f2,text="Name: " )
l6.grid(row =4, column =2 )
e2= tkinter.Entry(f2,width= 10)
e2.grid(row=4, column= 3)
#Representative and License #
l7 = tkinter.Label(f2,text="Representative:" )
l7.grid(row =5, column =0 )
e1 = tkinter.Entry(f2,width= 10)
e1.grid(row=5, column= 1)
l8 = tkinter.Label(f2,text="License #: " )
l8.grid(row =5, column =2 )
e2= tkinter.Entry(f2,width= 10)
e2.grid(row=5, column= 3)
#Location and Address
l9 = tkinter.Label(f2,text="Location:" )
l9.grid(row =6, column =0 )
e1 = tkinter.Entry(f2,width= 10)
e1.grid(row=6, column= 1)
l10 = tkinter.Label(f2,text="Address: " )
l10.grid(row =6, column =2 )
e2= tkinter.Entry(f2,width= 10)
e2.grid(row=6, column= 3)

#Cit/State/ZIP 
l11 = tkinter.Label(f2,text="Cit/State/ZIP:" )
l11.grid(row =7, column =0 )
e1 = tkinter.Entry(f2,width= 10)
e1.grid(row=7, column= 1)
l12 = tkinter.Label(f2,text="Cit/State/ZIP: " )
l12.grid(row =7, column =2 )
e2= tkinter.Entry(f2,width= 10)
e2.grid(row=7, column= 3)
#Phone 
l13 = tkinter.Label(f2,text="Phone:" )
l13.grid(row =8, column =0 )
e1 = tkinter.Entry(f2,width= 10)
e1.grid(row=8, column= 1)
l14 = tkinter.Label(f2,text="Phone: " )
l14.grid(row =8, column =2 )
e2= tkinter.Entry(f2,width= 10)
e2.grid(row=8, column= 3)

#VEHICAL INFORMATION
l15 = tkinter.Label(f3,text="Vehical Information " , font=("Arial", 20, 'bold'))
l15.grid(row =9, column =0 )
#VIN and Registration #
l16 = tkinter.Label(f3,text="VIN:" )
l16.grid(row =10, column =0 )
e1 = tkinter.Entry(f3,width= 10)
e1.grid(row=10, column= 1)
l17 = tkinter.Label(f3,text="Registration #: " )
l17.grid(row =10, column =2 )
e2= tkinter.Entry(f3,width= 10)
e2.grid(row=10, column= 3)
#Make and Model
l18 = tkinter.Label(f3,text="Make:" )
l18.grid(row =11, column =0 )
e1 = tkinter.Entry(f3,width= 10)
e1.grid(row=11, column= 1)
l19 = tkinter.Label(f3,text="Model: " )
l19.grid(row =11, column =2 )
e2= tkinter.Entry(f3,width= 10)
e2.grid(row=11, column= 3)
#Year and Mileage
l20 = tkinter.Label(f3,text="Year:" )
l20.grid(row =12, column =0 )
e1 = tkinter.Entry(f3,width= 10)
e1.grid(row=12, column= 1)
l21 = tkinter.Label(f3,text="Mileage: " )
l21.grid(row =12, column =2 )
e2= tkinter.Entry(f3,width= 10)
e2.grid(row=12, column= 3)
#Color
l22 = tkinter.Label(f3,text="Color: " )
l22.grid(row =13, column =0 )
e2= tkinter.Entry(f3,width= 10)
e2.grid(row=13, column= 1)






win.mainloop()

import tkinter
win = tkinter.Tk() # root base window
win.geometry("800x800")
f1 = tkinter.Frame(win)
f2 = tkinter.Frame(win)
f3 = tkinter.Frame(win)
f4 = tkinter.Frame(win)

#Label
f1.pack()
f2.pack()
f3.pack()
f4.pack()

#Tilte
l1 = tkinter.Label(f1,text="Title " , fg="black")
l1.grid(row =0, column =0 )
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=0, column= 3)

#Last Name 
l2 = tkinter.Label(f1,text="Last Name ")
l2.grid(row=1, column= 0)
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=1, column= 3)

#First Name(s)
l3 = tkinter.Label(f1,text="First Name(s) ")
l3.grid(row=2, column= 0)
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=2, column= 3)

#share with
l4 = tkinter.Label(f1,text="Share with " , fg="black")
l4.grid(row =3, column =0 )
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=3, column= 3)

#Business number
l5 = tkinter.Label(f1,text="Business Number " , fg="black")
l5.grid(row =4, column =0 )
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=4, column= 3)

#Mobile Number
l6 = tkinter.Label(f1,text="Mobile Number " , fg="black")
l6.grid(row =5, column =0 )
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=5, column= 3)

#Email Address
l7 = tkinter.Label(f1,text="Email Address " , fg="black")
l7.grid(row =6, column =0 )
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=6, column= 3)

#Date of Arrival
l8 = tkinter.Label(f1,text="Date of Arrival " , fg="black")
l8.grid(row =7, column =0 )
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=7, column= 3)

#Date of Departure
l9 = tkinter.Label(f1,text="Date of Departure " , fg="black")
l9.grid(row =8, column =0 )
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=8, column= 3)

#Name on Credit Card
l10 = tkinter.Label(f1,text="Name on Credit Card " , fg="black")
l10.grid(row =9, column =0 )
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=9, column= 3)

#Credit Card Number
l11 = tkinter.Label(f1,text="Credit Card Number " , fg="black")
l11.grid(row =10, column =0 )
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=10, column= 3)

#Expiry Date
l12 = tkinter.Label(f1,text="Expiry Date " , fg="black")
l12.grid(row =11, column =0 )
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=11, column= 3)

#CVV Number
l13 = tkinter.Label(f1,text="CVV Number " , fg="black")
l13.grid(row =12, column =0 )
e1 = tkinter.Entry(f1,width= 20)
e1.grid(row=12, column= 3)

#Payment Method

l14 = tkinter.Label(f1,text="Payment Method " , fg="black")
l14.grid(row=13, column=0)
c1 = tkinter.Checkbutton(f2, text="Credit Card")
c1.grid(row=13, column=1)
c2 = tkinter.Checkbutton(f2, text="Direct Bank Transfer")
c2.grid(row=13, column=2)

#negotiator
l15 = tkinter.Label(f2,text="Negotiated Rates:" , fg="black")
l15.grid(row=14, column=0)
#deluxe room
c1 = tkinter.Checkbutton(f2, text="Deluxe Room Single")
c1.grid(row=15, column=0)
l16 = tkinter.Label(f2, text = "Rs 1700")
l16.grid(row=15, column = 1)
c2 = tkinter.Checkbutton(f2, text="Deluxe Room Double")
c2.grid(row=15, column=2)
l17 = tkinter.Label(f2, text = "Rs 1800")
l17.grid(row=15, column = 3)
#suites room
c1 = tkinter.Checkbutton(f2, text="Suites Room Single")
c1.grid(row=16, column=0)
l16 = tkinter.Label(f2, text = "Rs 1700")
l16.grid(row=16, column = 1)
c2 = tkinter.Checkbutton(f2, text="Suites Room Double")
c2.grid(row=16, column=2)
l17 = tkinter.Label(f2, text = "Rs 1800")
l17.grid(row=16, column = 3)

#room preference
l15 = tkinter.Label(f2,text="Room Preference:" , fg="black")
l15.grid(row=17, column=0)
#Bed
c1 = tkinter.Checkbutton(f2, text="King Bed")
c1.grid(row=18, column=0)
c2 = tkinter.Checkbutton(f2, text="Twin- Two Single Beds")
c2.grid(row=18, column=2)

#1st para
l16 = tkinter.Label(f3,text="The above rates are quoted per room, per night. The rates include breakfast, 14% vat, and Excludes 1% Tourism Levy\n and a voluntary R10 donation to the Arabella Community Trust that will be levies onto your account." , fg="black")
l16.grid(row =21, column =0 )

#total amount
# Total amount payable      ZAR___ x___ nights = ZAR___ due to Arabella
l15 = tkinter.Label(f3,text="Total amount payable      ZAR_______ x______ nights = ZAR________ due to Arabella" , fg="black")
l15.grid(row=24, column=0)
# #zar
# c1 = tkinter.Checkbutton(f2, text="King Bed")
# c1.grid(row=18, column=0)
# c2 = tkinter.Checkbutton(f2, text="Twin- Two Single Beds")
# c2.grid(row=18, column=2)

l16 = tkinter.Label(f3,text="Credit Card will be charged on receipt of this form and details will also be used to settle all incidentals not settle on\n departure. A copy of the final folio will be sent to you should there be any unsettled charges" , fg="black")
l16.grid(row=25, column=0)

l17 = tkinter.Label(f3,text="In order to qualify for the above rates, your booking needs to be made on or before 15th January 2016" , fg="black")
l17.grid(row=26, column=0)

l18 = tkinter.Label(f3,text="Terms and conditions can be found on the next page." , fg="black")
l18.grid(row=27, column=0)

l19 = tkinter.Label(f3,text="The rate is valid for seven days before and after the conference dates. Check in time is 14:00 & check out time is 11:00" , fg="black")
l19.grid(row=28, column=0)

l20 = tkinter.Label(f3,text="By your signature hereto, you are accepting all terms and conditions specified on this form and confirm that all information\n given is current and accurate." , fg="black")
l20.grid(row=29, column=0)


#Tilte
l21 = tkinter.Label(f4,text="Signature " , fg="black")
l21.grid(row =30, column =0 )
e1 = tkinter.Entry(f4,width= 20)
e1.grid(row=30, column= 3)
l22 = tkinter.Label(f4,text="    Print Name" , fg="black")
l22.grid(row =30, column =5 )
e1 = tkinter.Entry(f4,width= 20)
e1.grid(row=30, column= 7)
l23 = tkinter.Label(f4,text="Date " , fg="black")
l23.grid(row =31, column =0 )
e1 = tkinter.Entry(f4,width= 20)
e1.grid(row=31, column= 3)



win.mainloop()
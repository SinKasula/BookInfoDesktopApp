"""
My Code for a database app - a basic one
user ca see all records, insert records,delete a record, update a record
Author: skasula
date : 10.11.18
"""

from tkinter import *

window = Tk()
l1 = Label(window, text = "Title")
l1.grid(row=0, column=0,pady=6)
e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value )
e1.grid(row=0, column=1,pady=6)
l2 = Label(window, text = "Author")
l2.grid(row=0, column=2, pady=6)
e2_value =  StringVar()
e2 = Entry(window ,textvariable = e2_value )
e2.grid(row=0, column=3,pady=6)

l3 = Label(window, text = "Year")
l3.grid(row=1, column=0,pady=6)
e3_value =  StringVar()
e3 = Entry(window, textvariable = e3_value  )
e3.grid(row=1, column=1,pady=6)
l4 = Label(window, text = "ISBN")
l4.grid(row=1, column=2,pady=6)
e4_value =  StringVar()
e4 = Entry(window, textvariable = e4_value )
e4.grid(row=1, column=3,pady=6)

#t1 = Text(window, height = 10, width = 30)
#t1.grid(row =2, column =0, rowspan = 3, columnspan = 2)

list1 = Listbox(window, height=10, width = 35)
list1.grid(row = 2, column = 0,  rowspan = 8, columnspan = 2 , pady =4)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column= 2 , rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window, text="View All", width = 12)
b1.grid(row=2 , column = 3, pady = 4, columnspan= 2)
b2 = Button(window, text="Search", width = 12)
b2.grid(row=3 , column = 3, pady = 4, columnspan= 2)
b3 = Button(window, text="Add", width = 12)
b3.grid(row=4 , column = 3, pady = 4, columnspan= 2)
b4 = Button(window, text="Update", width = 12)
b4.grid(row=5 , column = 3, pady = 4,  columnspan= 2)
b5 = Button(window, text="Delete", width = 12)
b5.grid(row=6 , column = 3, pady = 4, columnspan= 2)
b5 = Button(window, text="Close", width = 12)
b5.grid(row=7 , column = 3, pady = 4, columnspan= 2)



window.mainloop()

import tkinter
from tkinter import *
window = Tk()
window.geometry("500x400+400+200")
window.title("My First GUI")


Label(window, text='Username').grid(row=0)
Label(window, text='Password').grid(row=1)
e1 = Entry(window)
e2 = Entry(window, show = "*", width=20)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


txtfld = Entry(window, border = 5)
txtfld.place(x= 150, y = 220 )

lbl = Label(window, text= "My First Demo", font = "Verdana")
lbl.place(x = 150, y = 200)

btn1 = Button(window, text = "Login" , fg = "Black" , bg = "White")
btn1.place (x = 25, y = 50)


window.mainloop()

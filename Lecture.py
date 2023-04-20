from tkinter import *
win = Tk()
win.geometry("500x400+10+10")

lbl = Label(win, text = "Gender")
lbl.place(relx = 100, rely = 250)
lbl.pack(anchor = "center")

var1 = IntVar()
var2 = IntVar()

# create a radio button

r1 = Radiobutton(win, text = "Male", variable = var1)
r1.place(x = 50, y =50)

r2 = Radiobutton(win, text = "Female", variable = var2)
r2. place(x = 50, y = 75)

chk1 = Checkbutton(win, text = "100-200")
chk1.place(x = 70, y= 100)
chk2 = Checkbutton(win, text = "201-300")
chk2.place(x = 70, y= 120)
chk3 = Checkbutton(win, text = "301-400")
chk3.place(x = 70, y= 140)

lbl2 = Label(win, text = "Select from list of fruits")
lbl2.place (x= 80, y = 180)

lst = Listbox(win, selectmode = "Single")
lst.insert(1, "Mango")
lst.insert(2, "Orange")
lst.insert(3, "Apple")
lst.place(x = 80, y = 200)

win.mainloop()



from tkinter import *
class MyWindow:
    def __init__(self, window):
        self.lbl = Label(window, text='My Full Name')
        self.lbl.place(x=235, y=25)
        self.lbl1 = Label(window, text='Enter Given Name: ')
        self.lbl1.place(x=150,y=50)
        self.lbl2 = Label(window, text='Enter Middle Name: ')
        self.lbl2.place(x=150,y=100)
        self.lbl3 = Label(window, text="Enter Last Name: ")
        self.lbl3.place(x=150,y=150)
        self.lbl4 = Label(window, text="My Full Name is: ")
        self.lbl4.place(x=150,y=200)
        self.txt1 = Entry(window, bd=3)
        self.txt1.place(x=275, y=50)
        self.txt2 = Entry(window, bd=3)
        self.txt2.place(x=275, y=100)
        self.txt3 = Entry(window, bd=3)
        self.txt3.place(x=275, y=150)
        self.txt4 = Entry(window, bd=3, width = 27)
        self.txt4.place(x=275, y=200)

        self.btn_full_name = Button(window, text="Show Full Name")
        self.btn_full_name.place(x=235, y=250)

        self.btn_full_name.bind('<Button-1>',self.show_the_full_name)

    def show_the_full_name(self,fullname):
        self.txt4.delete(0, 'end')
        name1 = str(self.txt1.get())
        name2 = str(self.txt2.get())
        name3 = str(self.txt3.get())
        result = name1 + " " + name2 + " " + name3
        self.txt4.insert(END, str(result))



window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()
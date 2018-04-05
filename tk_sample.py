
from tkinter import *
import tkinter as ttk
import tkinter as tk



class MAIN:
    def __init__(self):
        self.master = master
        self.master.geometry('300x300')

        self.master.title('сalculator')
        self.but_1 = Button(self.master, text='1', width=2, height=10, bg='green', fg='black').grid(row=1, column=1)

        self.but_2 = Button(self.master, text='2', width=2, height=10, bg='green', fg='black')

        self.but_3 = Button(self.master, text='3', width=10, height=10, bg='yellow', fg='black')

        self.but_4 = Button(self.master, text='4', width=10, height=10, bg='green', fg='black')

        self.but_5 = Button(self.master, text='5', width=10, height=10, bg='green', fg='black')

        self.but_6 = Button(self.master, text='6', width=40, height=21, bg='green', fg='black')

        self.input = IntVar()
        self.entry = ttk.Entry(self.master, textvariable=self.input)

    def one(event):
        self.number == 1
    def two(event):
        self.number == 2
    def three(event):
        self.number == 3
    def four(event):
        self.number == 4
    def five(event):
        self.number == 5
    def six(event):
        self.number == 6
    def seven(event):
        self.number == 7
    def eight(event):
        self.number == 8
    def nine(event):
        self.number == 9

    def plus(event):
        self.number + number
    def zero(event):
        self.number - number





'''but_7=Button(root,text='7',width=40,height=21,bg='green',fg='black')
but_7.bind('<Button-7>',one)
but_7.place(x = 190, y = 40, width = 30)
but_8=Button(root,text='8',width=40,height=21,bg='green',fg='black')
but_8.bind('<Button-8>',one)
but_8.pack()

but_9=Button(root,text='9',width=40,height=21,bg='green',fg='black')
but_9.bind('<Button-9>',one)
but_9.pack()'''

def main():
    root = tk.Tk()


    root.mainloop()


if __name__ == '__main__':
    main()
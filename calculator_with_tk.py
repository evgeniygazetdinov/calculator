import tkinter
from tkinter import *

numbers = ['one','two','three','four'
	   'five','six','seven','eight','nine']

def find_number(event):
	for number in numbers:
		for i in range(9):
			number == i

def plus(event):
	number + number
	
def zero(event):
	number - number


root = Tk()
#replace to one func
but_1=Button(root,text='1',width=2,height=10,bg='green',fg='black')
but_1.bind('<Button-1>',one)
but_1.place(x =100, y = 10, width = 30,bordermode="outside")

but_2=Button(root,text='2',width=2,height=10,bg='green',fg='black')
but_2.bind('<Button-2>',one)
but_2.place(x = 130, y = 10, width = 30)

but_3=Button(root,text='3',width=10,height=10,bg='yellow',fg='black')
but_3.bind('<Button-3>',one)
but_3.place(x = 160, y = 10, width = 30)

but_4=Button(root,text='4',width=10,height=10,bg='green',fg='black')
but_4.bind('<Button-4>',one)
but_4.place(x = 100, y = 40, width = 30)

but_5=Button(root,text='5',width=10,height=10,bg='green',fg='black')
but_5.bind('<Button-5>',one)
but_5.place(x = 130, y = 40, width = 30)

but_6=Button(root,text='6',width=40,height=21,bg='green',fg='black')
but_6.bind('<Button-5>',one)
but_6.place(x = 160, y = 40, width = 30)

'''but_7=Button(root,text='7',width=40,height=21,bg='green',fg='black')
but_7.bind('<Button-7>',one)
but_7.place(x = 190, y = 40, width = 30)
but_8=Button(root,text='8',width=40,height=21,bg='green',fg='black')
but_8.bind('<Button-8>',one)
but_8.pack()

but_9=Button(root,text='9',width=40,height=21,bg='green',fg='black')
but_9.bind('<Button-9>',one)
but_9.pack()'''
root.mainloop()



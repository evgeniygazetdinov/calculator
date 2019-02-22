import tkinter
from tkinter import *

numbers = ['one','two','three','four'
	   'five','six','seven','eight','nine']
def main():
    root = Tk()
    draw_buttons(root)
    root.mainloop()

def find_number(event):
	for number in numbers:
		for i in range(9):
			number == i
def draw_buttons(root):
    for number in numbers:
        but = Button(root, text='{}'.format(len(number), width=2, height=10, bg='green', fg='black'))
    for i in range(5):
        for x in range(10):
            but.grid(row = x,column = i)

def plus(event):
	number + number

def zero(event):
	number - number

if __name__ == "__main__":
	main()


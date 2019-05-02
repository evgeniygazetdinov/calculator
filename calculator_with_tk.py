from Tkinter import *

numbers = ['one','two','three','four'
	   'five','six','seven','eight','nine']
def main():
    root = Tk()
    dispay = Entry(root,)
    dispay.grid(row=4,column=0 ,columnspan = 4)
    dispay.insert(0,1)
    draw_numbers(root)
    root.mainloop()

def find_number(event):
	for number in numbers:
		for i in range(9):
			number == i
def draw_numbers(root):
    buttons = list()
    for i in range(0,10,1):
        buttons.append(Button(root, text='{}'.format(str(i), width=2, height=10, bg='green', fg='black',command = lambda i: dispay.insert(0,i))))
        buttons[-1].grid(row =0,column=i,sticky = N+E+S+W)
        if i >3 :
            buttons[-1].grid(row =1,column=i-3)
        if i >6 :
            buttons[-1].grid(row =2,column=i-6)

def draw_symbols(root):
    symbols = list()

def show(root):
    pass

def plus(event):
	number + number

def zero(event):
	number - number

if __name__ == "__main__":
	main()



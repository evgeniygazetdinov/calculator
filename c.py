# -*- coding: utf-8 -*-

import tkinter as tk

operation = tk.StringVar()

def equlize():
    f_n = first_number.get()
    s_n = second_number.get()
    operator = operation.get()`


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()
first_number = tk.Entry (root)
canvas1.create_window(210, 100, window=entry1)
second_number = tk.Entry (root)
canvas1.create_window(210, 100, window=entry1)
#operations
divider = tk.Button(root,name = '/',command = lambda :operation.set('/'))
canvas1.create_window(220, 110, window=but)
multiply = tk.Button(root,name = '*',command = lambda :operation.set('*'))
canvas1.create_window(220, 110, window=but)
plus = tk.Button(root,name = '+',command =lambda :operation.set('+'))
canvas1.create_window(220, 110, window=but)
eq = tk.Button(root,name = '=',command = equlize)
canvas1.create_window(220, 110, window=but)
root.mainloop()

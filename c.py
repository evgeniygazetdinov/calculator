# -*- coding: utf-8 -*-

import tkinter as tk

def fin():
    print(entry1.get())

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()
entry1 = tk.Entry (root)
canvas1.create_window(210, 100, window=entry1)
but = tk.Button(root,command =fin)
canvas1.create_window(220, 110, window=but)



root.mainloop()

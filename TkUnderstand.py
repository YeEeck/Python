from tkinter import *
from tkinter import ttk

def replace1(text):
    t2.set(text)
    return 'ok'

def Button_back1():
    p = replace1(t1.get())
    t1.set(p)


root = Tk()
t1 = StringVar()
e1 = ttk.Entry(root, textvariable=t1)
e1.grid()
t2 = StringVar()
e2 = ttk.Entry(root, textvariable=t2)
e2.grid()
ttk.Button(text='按钮', command=Button_back1).grid(row=3)
mainloop()



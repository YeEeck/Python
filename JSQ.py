from tkinter import *
from tkinter import ttk
import win32api

def a(n, x, m):
    if x == '+':
        b = n+m
        print(b)
        return b
    elif x == '-':
        b = n-m
        return b
    elif x == '*':
        b = n*m
        return b
    elif x == '÷':
        b = n/m
        return b

def Button_back1():
    t3.set(a(float(e1.get()), name.get(), float(e2.get())))

def Button_back2():
    e1.delete(0, END)
    e2.delete(0, END)
    t3.set('')

def Button_back3():
    win32api.MessageBox(0, '计算结果已复制', '成功')

root = Tk()
root.title('计算器Demo')
e1 = ttk.Entry(root, width=8, justify='center')
e1.grid()
e2 = ttk.Entry(root, width=8, justify='center')
e2.grid(row=0, column=2)
name = StringVar()
numberChosen = ttk.Combobox(root, width=1, textvariable=name, state='readonly')
numberChosen['values'] = ('+', '-', '*', '÷')     # 设置下拉列表的值
numberChosen.grid(column=1, row=0)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
ttk.Label(root, text='=', width=1).grid(row=0, column=3)
t3 = StringVar()
e3 = ttk.Entry(root, state='readonly', width=10, textvariable=t3, justify='center')
e3.grid(row=0, column=4)
ttk.Button(root, text='计算', command=Button_back1).grid(row=1, columnspan=2)
ttk.Button(root, text='清空', command=Button_back2).grid(row=1, column=2, columnspan=2)
ttk.Button(root, text='复制结果', command=Button_back3).grid(row=1, column=4, columnspan=1)
mainloop()
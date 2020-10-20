from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Billbook')
# 组件生成与设置
ttk.Label(root, text='金钱合计：', justify='center').grid(row=0, column=0)
v_sum = IntVar()
ttk.Entry(root, justify='center', state='readonly', width=5, textvariable=v_sum).grid(row=0, column=1)
ttk.Button(root, text='添加收入').grid(row=0, column=2, columnspan=2)
ttk.Label(root, text='他人欠款：').grid(row=1, column=0)
v_lend = IntVar()
ttk.Entry(root, justify='center', state='readonly', width=5, textvariable=v_lend).grid(row=1, column=1)
ttk.Button(root, text='详细', width=5).grid(row=1, column=2)
ttk.Button(root, text='添加', width=5).grid(row=1, column=3)
ttk.Label(root, text='欠他人款：', justify='center').grid(row=2, column=0)
v_borrow = IntVar()
ttk.Entry(root, justify='center', state='readonly', width=5, textvariable=v_borrow).grid(row=2, column=1)
ttk.Button(root, text='详细', width=5).grid(row=2, column=2)
ttk.Button(root, text='添加', width=5).grid(row=2, column=3)
ttk.Label(root, text='金钱剩余：', justify='center').grid(row=3, column=0)
v_remain = IntVar()
ttk.Entry(root, justify='center', state='readonly', width=5, textvariable=v_remain).grid(row=3, column=1)
ttk.Button(root, text='添加支出').grid(row=3, column=2, columnspan=2)
ttk.Button(root, text='收入详单').grid(row=4, column=0, columnspan=2)
ttk.Button(root, text='支出详单').grid(row=4, column=2, columnspan=2)

mainloop()

from tkinter import *
from tkinter import ttk


def dis(x, y, A, B, C=0):
    global v1
    d = (A * x + B * y + C) / (A * A + B * B) ** 0.5
    if ((A * A + B * B) ** 0.5) % 1 == 0:
        v1.set(str(d))
    else:
        p = str(A * x + B * y + C)
        v1.set('%s/√%s' % (p, A * A + B * B))
        # print('%s/√%s'%(p,A*A+B*B))


def button_back():
    global e1
    global e2
    global e3
    global e4
    global e5
    try:
        p = int(e5.get())
    except ValueError:
        p = 0
    t = map(int, [e1.get(), e2.get(), e3.get(), e4.get(), p])
    dis(next(t), next(t), next(t), next(t), next(t))


root = Tk()
root.title('点到直线的距离')
Label(root, text='点X坐标：', width=12).grid(row=0, column=0)
e1 = ttk.Entry(root, width=8)
e1.grid(row=0, column=1)
Label(root, text='点Y坐标：').grid(row=1, column=0)
e2 = ttk.Entry(root, width=8)
e2.grid(row=1, column=1)
v1 = StringVar()
v1.set('点到直线的距离计算')
Label(root, textvariable=v1).grid(row=5, column=0, columnspan=3)
Label(root, text='直线A参数：').grid(row=2)
e3 = ttk.Entry(root, width=8)
e3.grid(row=2, column=1)
Label(root, text='直线B参数：').grid(row=3)
e4 = ttk.Entry(root, width=8)
e4.grid(row=3, column=1)
Label(root, text='直线C参数：').grid(row=4)
e5 = ttk.Entry(root, width=8)
e5.grid(row=4, column=1)
Label(root, width=1).grid(row=0, column=2)
ttk.Button(root, text='计算', width=22, command=button_back).grid(row=6, column=0, columnspan=3)

mainloop()

from tkinter import *
from random import randint
from tkinter import ttk
import win32api


def randint_back():
    r = randint(1, 4)
    if r == 1:
        return 'A'
    elif r == 2:
        return 'B'
    elif r == 3:
        return 'C'
    else:
        return 'D'


def button_back():
    global v2
    global e1
    t = [randint_back() for i in range(0, int(e1.get()))]
    s = ''
    for p in t:
        s = s + ' ' + p
    judge(t, s)


def judge(t, s):
    numa = 0
    numc = 0
    numd = 0
    numb = 0
    if v2.get() == 1:
        for d in t:
            if d == 'A':
                numa = numa + 1
            elif d == 'B':
                numb = numb + 1
            elif d == 'C':
                numc = numc + 1
            else:
                numd = numd + 1
        p = (int(e2.get()) + 1) / 100
        if p <= (int(float(e1.get()) / 4) + 1) / 10:
            win32api.MessageBox(0, '容差率过小', '错误')
        else:
            if numa / int(e1.get()) >= p or numc / int(e1.get()) >= p or numb / int(e1.get()) >= p or numd / int(
                    e1.get()) >= p:
                button_back()
            else:
                v1.set(s)

    else:
        v1.set(s)


def checkbox_back():
    if v2.get() == 1:
        e2['state'] = 'normal'
    else:
        e2['state'] = 'disable'


root = Tk()
root.title('auto_answer')
v1 = StringVar()
v1.set('自动生成')
Label(root, textvariable=v1, width=20).grid(row=0, columnspan=3)
Label(root, text='生成数量:').grid(row=1, column=0)
e1 = ttk.Entry(root, justify='center', width=10)
e1.insert(0, '10')
e1.grid(row=1, column=1, columnspan=2)
ttk.Button(text='生成', width=20, command=button_back).grid(row=4, columnspan=3)
v2 = IntVar()
check1 = ttk.Checkbutton(root, text='更科学的生成规则', variable=v2, command=checkbox_back)
check1.grid(row=2, columnspan=3)
v2.set(1)
Label(text='容差率：').grid(row=3, column=0)
Label(text='%', width=1).grid(row=3, column=2)
e2 = ttk.Entry(justify='center', width=7)
e2.grid(row=3, column=1)
e2.insert(0, '50')
mainloop()

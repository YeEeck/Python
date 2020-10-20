from tkinter import *
from tkinter import ttk
import win32api
import pyperclip


def Button_back1():
    global t
    global e1
    s = ''
    for i in e1.get():
        p = str(hex(ord(i)))[2:]
        if len(p) == 2:
            p = '00' + p
        s = s + '\\u' + p
    s = '\'' + s + '\''
    t.set(s)


def Button_back2():
    global e2
    setText(e2.get())
    win32api.MessageBox(0, '%s 已置入到剪贴板' % e2.get(), '提示')


def setText(aString):  # 写入剪切板
    pyperclip.copy(aString)


def Button_back3():
    global e1
    e1.delete(0, END)
    t.set('')


root = Tk()
root.title('文本转16进制')
t = StringVar()
t.set('')
e1 = ttk.Entry(root, width=40, justify='center')
e2 = ttk.Entry(root, textvariable=t, width=40, justify='center')
# e1.insert(10, '这里是原文本')
e1.grid(row=0, column=0, columnspan=3)
e2.grid(row=2, column=0, columnspan=3)
e2['state'] = 'readonly'
ttk.Button(root, text='转换', width=13, command=Button_back1).grid(row=1, column=0)
ttk.Button(root, text='复制结果', width=13, command=Button_back2).grid(row=1, column=1)
ttk.Button(root, text='清空', width=13, command=Button_back3).grid(row=1, column=2)
mainloop()

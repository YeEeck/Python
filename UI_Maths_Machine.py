from tkinter import *
from tkinter import ttk
from random import randint
import os
import tkinter.messagebox as messagebox

Max = 10
Min = 1
difficulty = 1
Randnum1 = randint(Min, Max)
Randnum2 = randint(Min, Max)


def isnub(s):
    try:
        nb = float(s)  # 将字符串转换成数字成功则返回True
        return True
    except ValueError as e:
        return False  # 如果出现异常则返回False


def button_back1():
    num = e1.get()
    if num == '':
        messagebox.showinfo('警告', '请不要输入空数据')
    elif not isnub(num):
        messagebox.showinfo('警告', '请不要输入英文或不支持的符号')
    else:
        if int(num) == Randnum2 + Randnum1:
            global Exp
            global level
            global Max_Exp
            global d
            global difficulty
            global v3
            exp_up = 0
            if difficulty == 1:
                exp_up = 1
                Exp = Exp + exp_up
            elif difficulty == 2:
                exp_up = 5
                Exp = Exp + exp_up
            else:
                exp_up = 10
                Exp = Exp + exp_up
            messagebox.showinfo('恭喜', '回答正确\n经验+%s' % exp_up)
            level = exp2level(Exp)
            Max_Exp = d[level]
            v3.set('你的等级：%s  ----  经验值：%s/%s' % (level, Exp, Max_Exp))
            # Label(root, text='你的等级：%s  ----  经验值：%s/%s' % (level, Exp, Max_Exp)).grid(row=0, columnspan=2)
            button_back2()
        else:
            messagebox.showinfo('很遗憾', '回答错误')
            button_back2()


def button_back2():
    global Randnum1
    global Randnum2
    global Max
    global Min
    global v1
    Randnum1 = randint(Min, Max)
    Randnum2 = randint(Min, Max)
    v1.set('%s + %s =' % (Randnum1, Randnum2))
    # Label(root, text='%s + %s =' % (Randnum1, Randnum2)).grid(row=1)
    e1.delete(0, END)


def loading():
    with open('config.ini') as f:
        return f.readline()


def exp2level(exp):
    if exp >= 1000:
        return 10
    elif exp >= 750:
        return 9
    elif exp >= 500:
        return 8
    elif exp >= 350:
        return 7
    elif exp >= 250:
        return 6
    elif exp >= 150:
        return 5
    elif exp >= 100:
        return 4
    elif exp >= 50:
        return 3
    elif exp >= 25:
        return 2
    else:
        return 1


if not os.path.exists('config.ini'):
    with open('config.ini', 'w') as file:
        file.write('0')
with open('config.ini') as file:
    if file.read() == '':
        file.close()
        with open('config.ini', 'w') as file:
            file.write('0')


# 以下为调整难度的函数：
def difficulty2one():
    global Max
    global Min
    global difficulty
    Max = 10
    Min = 1
    difficulty = 1
    Label(root, text='难度：%s' % difficulty).grid(row=0, column=2)
    button_back2()


def difficulty2two():
    global Max
    global Min
    global difficulty
    Max = 25
    Min = 10
    difficulty = 2
    Label(root, text='难度：%s' % difficulty).grid(row=0, column=2)
    button_back2()


def difficulty2three():
    global Max
    global Min
    global difficulty
    global v2
    Max = 50
    Min = 25
    difficulty = 3
    v2.set('难度：%s' % difficulty)
    # Label(root, text='难度：%s' % difficuty).grid(row=0, column=2)
    button_back2()


root = Tk()
root.title('Maths_Machine')
menubar = Menu(root)
# root.geometry("200x100")

# 等级，经验值系统
Exp = int(float(loading()))
level = exp2level(Exp)
d = {1: 25, 2: 50, 3: 100, 4: 150, 5: 250, 6: 350, 7: 500, 8: 750, 9: 1000, 10: ''}
Max_Exp = d[level]
v3 = StringVar()
v3.set('你的等级：%s  ----  经验值：%s/%s' % (level, Exp, Max_Exp))
Label(root, textvariable=v3).grid(row=0, columnspan=2)

# 顶端菜单
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label='退出', command=root.quit)
menubar.add_cascade(label='选项', menu=menu1)
menu2 = Menu(root, tearoff=0)
menu2.add_command(label='难度一(20以内)', command=difficulty2one)
menu2.add_command(label='难度二(50以内 不包括20以下)', command=difficulty2two)
menu2.add_command(label='难度三(100以内)', command=difficulty2three)
menubar.add_cascade(label='难度调整', menu=menu2)

root.config(menu=menubar)  # 显示这个菜单

# 新建的各种组件(标签，输入框，按钮)
v2 = StringVar()
v2.set('难度：%s' % difficulty)
Label(root, textvariable=v2).grid(row=0, column=2)
v1 = StringVar()
v1.set('%s + %s =' % (Randnum1, Randnum2))
L1 = Label(root, textvariable=v1).grid(row=1)
e1 = ttk.Entry(root)
e1.grid(row=1, column=1)
# Button(root,command=button_back2,text='     刷新     ').grid(row=2,column=0)
ttk.Button(root, command=button_back1, text='    提交   ').grid(row=1, column=2)
mainloop()

# 结束后的保存工作
with open('config.ini', 'w') as f:
    f.write(str(Exp))

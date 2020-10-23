Moneystr = input("请输入带有符号的货币金额(人民币为Y 美元为D):")
if Moneystr[-1] in ['Y', 'y']:
    D = eval(Moneystr[0:-1]) / 6
    print(Moneystr[0:-1] + "元人民币等价为{:.2f}元美元".format(D))
elif Moneystr[-1] in ['D', 'd']:
    Y = eval(Moneystr[0:-1]) * 6
    print(Moneystr[0:-1] + "元美元等价为{:.2f}元人民币".format(Y))
else:
    print("输入数据错误")

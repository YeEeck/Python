Tempnum = eval(input('请输入不带符号的温度值:'))
Tempsyn = input('请输入温度符号(摄氏度为C，华氏度为F):')
if Tempsyn in ['F', 'f']:
    C = (Tempnum - 32) / 1.8
    print("转换后的温度是{:d}C".format(int(C)))
elif Tempsyn in ['C', 'c']:
    F = Tempnum * 1.8 + 32
    print("转换后的温度是{:d}F".format(int(F)))
else:
    print("输入格式错误")

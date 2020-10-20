print('欢迎使用')
print('解析几何对称点计算启动')
# 获取必要数据
x1 = int(input('请输入第一个点的X坐标：'))
y1 = int(input('请输入第一个点的Y坐标：'))
line1_1 = int(input('请输入直线的一次项系数：'))
line1_2 = int(input('请输入直线的常数项：'))
# 计算第二条直线斜率
line2_1 = (-1)/line1_1
# 计算第二条直线常数项
line2_2 = y1-line2_1*x1
# 计算两直线焦点
dot_x = (line1_2+line2_2)/(line1_1-line2_1)
dot_y = line1_1*dot_x+line1_2
# 将焦点作为中点 计算对称点
x2 = 2*dot_x-x1
y2 = 2*dot_y-y1
# 格式化输出
print('\n点(%s,%s)关于直线y=%sx+%s的对称点为(%s,%s)' % (x1, y1, line1_1, line1_2, x2, y2))
print('\n附：\n第二条直线方程：y=%sx+%s\n焦点坐标：(%s,%s)' % (line2_1, line2_2, dot_x, dot_y))
input('按任意键结束')

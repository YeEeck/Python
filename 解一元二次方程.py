import math
def hs(a, b, c):
    d = float(b)*float(b)-4*float(a)*float(c)
    print('△ = %s' % str((float(b)*float(b)-4*float(a)*float(c))))
    if d < 0:
        print('∵△ < 0')
        print('∴该方程无解')
    elif d == 0:
        s = -float(b)/2*a
        print('∵△ = 0')
        print('∴该方程有唯一解，为%s'% s)
    else:
        s1 = (-float(b)+ math.sqrt(float(d)))/2*float(a)
        s2 = (-float(b)- math.sqrt(float(d)))/2*float(a)
        print('∵△ > 0')
        print('∴该方程有两根，分别为%s与%s' % (s1, s2))

print('---一元二次方程计算器开始运行---')
p = input('请问你是否通过命令行启动（是为Y，否为N）：')
a = input('请输入二次项系数：')
b = input('请输入一次项系数：')
c = input('请输入常数项：')
hs(a, b, c)
if p == 'N':
    pass
elif p == 'n':
    pass
else:
    input()

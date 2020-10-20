import math
def hs(a,b,c):
	a=float(a)
	b=float(b)
	c=float(c)
	if a==0:
		print('该函数不是二次函数!')
	else:
		Sa = -b / 2 * a
		print('\n-对称轴：X=%s' % Sa)

		if a < 0:
			tw = '向下'
		else:
			tw = '向上'
		print('\n-开口方向：%s' % tw)

		print('\n-定义域：R')

		min_max = a * Sa * Sa + b * Sa + c
		if a>0:
			print('\n-值域：(%s,+∞)'%min_max)
		else:
			print('\n-值域：(-∞,%s)'%min_max)

		print('\n-顶点：(%s,%s)'%(Sa,min_max))

		print('\n-零点：')
		d = b * b - 4 * a * c
		if d < 0:
			print('该函数不存在零点')
		elif d == 0:
			s = -b / 2 * a
			print('该一元二次方程有一个零点，为(%s,0)' % s)
		else:
			s1 = (-b + math.sqrt(d)) / 2 * a
			s2 = (-b - math.sqrt(d)) / 2 * a
			print('该一元二次方程有两个零点，分别为(%s,0)与(%s,0)' % (s1, s2))

print('---二次函数解析开始运行---')
a = input('请输入二次项系数：')
b = input('请输入一次项系数：')
c = input('请输入常数项：')
hs(a, b, c)
input()

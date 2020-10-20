def gcd(a, b):
	a = int(a)
	b = int(b)
	while a % b != 0:
		save = a
		a = b
		b = save % b
	return b


a = input('请输入第一个数：')
b = input('请输入第二个数：')
print('公约数为：%s' % gcd(a, b))

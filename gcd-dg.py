def gcd(a,b):
	if a%b==0:
		return b
	else:
		return (gcd(b,a%b))

a=input('请输入第一个数：')
b=input('请输入第二个数：')
print('公约数为：%s'%gcd(int(a),int(b)))
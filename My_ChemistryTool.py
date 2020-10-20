# 如题，这是一个帮助化学方程配平的脚本
equation = input('请输入化学方程式（例：O2+H2=H2O）:')
place_balance = equation.find('=')
place1 = 0
place1_sum = []
place1_sum.append(place1-1)
place1 = equation.find('+', place1+1, place_balance)
while place1 != -1:
    place1_sum.append(place1)
    place1 = equation.find('+', place1+1, place_balance)

place1_sum.append(place_balance)
place1_text = []
for i in range(len(place1_sum)-1):
    place1_text.append(equation[place1_sum[i-1] + 1:place1_sum[i]])
    print(equation[place1_sum[i-1] + 1:place1_sum[i]])
print('反应物为%s个物质' % (len(place1_sum)-1))

place2 = place_balance
place2_sum = []
place2_sum.append(place2)
place2 = equation.find('+', place_balance, )
while place2 != -1:
    place2_sum.append(place2)
    place2 = equation.find('+', place2+1, )
place2_sum.append(len(equation))
place2_text = []
for t in range(len(place2_sum)-1):
    place2_text.append(equation[place1_sum[t] + 1:place1_sum[t+1]])
    print(equation[place2_sum[t] + 1:place2_sum[t+1]])

# O2+H2+co2=H2O+co
'''
place2 = 0
place2_sum = []
while place2 != -1:
    place2 = equation.find('+', place_balance, )
    place2_sum.append(place2)
'''
print('生成物为%s个物质' % len(place2_sum))
# print(equation[place1_sum[0]+1:place1_sum[1]])
# print(equation[place1_sum[1]+1:place1_sum[2]])
# print(equation[place1_sum[2]+1:place1_sum[3]])

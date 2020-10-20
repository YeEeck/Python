import random
def roll(t):
    i=0
    j=[]
    while i<=t:
        i=i+1
        s_roll = random.randint(1, 100)
        if s_roll == 100:
            j.append('SSR')
        elif s_roll <= 5:
            j.append('SR')
        else:
            j.append('R')
    return j
t=int(input('请输入抽奖的次数：'))
for k in roll(t):
    print('你获得了：%s'%k)
input()
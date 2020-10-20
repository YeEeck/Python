B=[] #设置操作过程列表
def move(n, a, b, c):
if n==1:
    buzhou=a+str(n)+'-->'+c+str(n) #一个圆盘需要从A到C操作步骤
    B.append(buzhou) #向列表中添加操作步骤
    return
move(n-1,a,c,b) #将A柱的n-1个盘移到B柱
buzhou=a+str(n)+'-->'+c+str(n) #将A柱的第n个盘移到C柱操作步骤
B.append(buzhou) #向列表中添加操作步骤
move(n-1,b,a,c) #将过渡柱子B上n-1个圆盘B移动到目标柱子C
move(6，'A','B','C') #2**64-1，64次太大，这里用6个盘子
print('共需操作'+str(len(B))+'次','操作过程为',B)#计算6个盘子的步骤数及操作过程

height = float(input("身高(cm)：")) / 100
weight = float(input("体重(斤)：")) / 2
bmi = weight / (height * height)
print('bmi值=%s' % bmi)
if bmi < 18.5:
    print("过轻")
elif bmi <= 25:
    print("正常")
elif bmi <= 28:
    print("过重")
elif bmi <= 32:
    print("肥胖")
else:
    print("严重肥胖")
input()

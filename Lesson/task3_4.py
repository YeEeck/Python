while 1:
    num_str1 = input("请输入一个5位数字：")
    if num_str1 in ["STOP", "Stop", "stop"]:
        break
    if num_str1.isdigit() == 0:
        continue
    num_str2 = num_str1[::-1]
    if eval(num_str1) == eval(num_str2):
        print("是回文数")
    else:
        print("不是回文数")

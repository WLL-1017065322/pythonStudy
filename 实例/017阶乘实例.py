

def factorial(num):
    if num < 0:
        return print("负数没有阶乘")
    result = 1
    for i in range(1,num + 1):
        result =result * i
    # print("{0} 的阶乘是：{1}".format(num,result))
    print("%d 的阶乘是：%d"%(num, result))

num = int(input("输入数字"))
factorial(num)
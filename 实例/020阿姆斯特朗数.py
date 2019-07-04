
# 判断是否是阿姆斯特朗数
def is_amstl(num):
    # if num < 10 and num > 0:
        # print("%d是阿姆斯特朗数"%num)

    if num > 0:
        n = len(str(num))   # 返回长度
        sum = 0
        temp = num
        while temp >0:
            digit = temp % 10
            sum += digit ** n
            temp //= 10
        if sum ==num:
            print("%d是阿姆斯特朗数"%num)
        else:
            print("%d不是阿姆斯特朗数"%num)





#输出阿姆斯特朗数

def get_amstls(min,max):
    for num in range(min,max+1):
        sum = 0
        n=len(str(num))

        temp = num

        while temp>0:
            a = temp % 10
            sum += a ** n
            temp //= 10

        if num == sum:
            print(num)



# num = int(input("输入数字"))

# print(len(str(num)))
# is_amstl(num)

min = int(input("输入最小值"))
max = int(input("输入最大值"))
get_amstls(min,max)
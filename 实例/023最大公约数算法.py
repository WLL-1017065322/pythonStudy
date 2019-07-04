

def hcf(a,b):
    for i in range(1,a):

        if a % i ==0 and b % i ==0:
            # print(i)
            # break
            hcf = i

    print("{0}和{1}最大公约数是:{2}".format(a,b,hcf))


a = int(input("输入第一个数："))
b = int(input("输入第二个数："))
hcf(a,b)
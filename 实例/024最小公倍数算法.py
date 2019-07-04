

def lcm(a,b):

    for i in range(1,a*b):
        if i % a ==0 and i % b ==0:
            print("{0}和{1}最小公倍数是：{2}".format(a,b,i))
            break



a = int(input("输入第一个数："))
b = int(input("输入第二个数："))
lcm(a,b)
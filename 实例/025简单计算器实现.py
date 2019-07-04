
# 加
def add(x,y):
    return x+y
# 减
def subtract(x,y):
    return x-y
# 乘
def multiply(x,y):
    return x * y
# 除
def divide(x,y):
    return x/y


print("选择运算：1：加，2：减，3：乘，4：除")
choice = int(input("输入你的选择：1/2/3/4："))
x = int(input("输入x的值"))
y = int(input("输入y的值"))

if choice == 1:
    print("{0}和{1}的和是：{2}".format(x,y,add(x,y)))

elif choice == 2:
    print("{0}和{1}的和是：{2}".format(x, y, subtract(x,y)))

elif choice == 3:
    print("{0}和{1}的和是：{2}".format(x, y, multiply(x,y)))

elif choice == 4:
    print("{0}和{1}的和是：{2}".format(x, y, divide(x,y)))

else:
    print("非法输入")

#使用中间变量

# a = float(input("a的值"))
#
# b = float (input("b的值"))
#
# temp = a
#
# a = b
#
# b = temp
#
# print("交换后a的值:%.1f"%a)
#
# print("交换后b的值:%.1f"%b)


#不使用中间变量


a = float(input("a的值"))

b = float (input("b的值"))

a,b = b,a


print("交换后a的值:{}".format(a))
print("交换后b的值:{}".format(b))
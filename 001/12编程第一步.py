# 在前面的教程中我们已经学习了一些 Python3 的基本语法知识，下面我们尝试来写一个斐波纳契数列。

# a,b = 0,1
# while b<10:
#     print(b)
#     a,b =b,a+b
#


a, b = 0, 1
while b < 10:
    print(b,end = ',')
    a, b = b, a + b

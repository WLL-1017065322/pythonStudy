def addList(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum
#
def addList2(lst):
    sum = 0
    for ele in range(0,len(lst)):
        sum = sum + lst[ele]
    return sum
# 使用while循环
def addList3(lst):
    ele = 0
    sum = 0
    while (ele < len(lst)):
        sum = sum + lst[ele]
        ele += 1
    return sum
# 使用递归
def addList4(lst,n):
    if (n == 0):
        return 0
    else:
        return lst[n - 1] + addList4(lst,n - 1)
lst = [11, 5, 17, 18, 23]
sum = addList4(lst,len(lst))
print(addList(lst))
print(addList2(lst))
print(addList3(lst))
print(sum)
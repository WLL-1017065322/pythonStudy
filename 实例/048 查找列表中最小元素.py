def minNum(lst):
    min = lst[0]
    for i in lst:
        if(i < min):
            min = i
    return min
# 改进版
def minNum1(lst):
    min = lst[0]
    sub = 0
    for ele in range(0,len(lst)):
        if(min > lst[ele]):
            min = lst[ele]
            sub = ele + 1
    return (min,sub)
# sort()
def minNum2(lst):
    lst.sort()
    return lst[0:1]
    # return lst
# min()
def minNum3(lst):
    return min(lst)
list1 = [10, 20, 4, 45, 99]
print(minNum(list1))
print(minNum1(list1))
print(minNum2(list1))
print(minNum3(list1))
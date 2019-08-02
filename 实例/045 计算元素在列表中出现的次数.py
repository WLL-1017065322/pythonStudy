# 循环
def count1(lst,num):
    count = 0
    for i in lst:
        if (num == i):
            count += 1
    # print(count)
    return count

#count
def count2(lst,num):
    return lst.count(num)


lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# count1(lst,10)
print(count1(lst,10))
print(count2(lst,15))
# 使用循环
def search(num,list):
     for i in list:
         if (i == num):
            print("存在1")
      # return print("不存在")
     # print("查看 4 是否在列表中 ( 使用 in 关键字 ) ")

# 使用 in 关键字
def search2(num, list):
    if(num in list):
        print("存在2")
    else:
        print("不存在2")

# 使用 set() + in

def search3(num,list):
    list = set(list)
    if num in list:
        print("存在3")

# 使用 sort() + bisect_left()
from bisect import bisect_left
def search4(num,list):
    list.sort()
    if bisect_left(list,num):
        print("存在4")

list = [ 1, 6, 3, 5, 3, 4 ]
list3 = [ 1, 6, 3, 5, 3, 4 ]
search(1 ,list)
search2(7 ,list)
search3(1 ,list3)
search4(1 ,list)
# [:]
def clone_list1(lst):
    lst_copy = lst[:]
    return lst_copy
# xx.extend()
def clone_list2(lst):
    li_copy = []
    li_copy.extend(lst)
    return li_copy
#list()
def clone_list3(lst):
    li_copy = list(lst)
    return li_copy

li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_list1(li1)
li3 = clone_list2(li1)
li4 = clone_list3(li1)
print(li2)
print(li3)
print(li4)





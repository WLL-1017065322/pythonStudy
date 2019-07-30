def Reverse(list):
    return [ele for ele in reversed(list)]


def Reverse2(list):
    list.reverse()
    return list

def Reverse4(list):
    new_list = list[::-1]
    return  new_list

list = [10, 11, 12, 13, 14, 15]
#[x:y:z]切片索引,x是左端,y是右端,z是步长,在[x,y)区间从左到右每隔z取值,默认z为1可以省略z参数.
# 步长的负号就是反向,从右到左取值.
# 切片的语法表达式为：[start_index : end_index : step]，其中：
# start_index表示起始索引
# end_index表示结束索引
# step表示步长，步长不能为0，且默认值为1
# [::-1]切片意思是从列表最后一位开始，步长为-1，即从[-1]开始，索引值每次累加-1，累加值为-7时结束,用一个函数来表示：
# def daoxu(l):
# ll = []
# n = -1
# while True:
# ll.append(l[n])
# n -= 1
# if len(ll) == len(l):
# break
# return ll
print(Reverse(list))
print(Reverse2(list))
print(Reverse4(list))
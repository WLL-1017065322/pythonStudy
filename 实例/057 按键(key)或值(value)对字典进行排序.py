def dictionairy():
    # 声明字典
    key_value = {}

    # 初始化
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
    print("按键(key)排序:")
    # 字典按键排序
    # for i in sorted(key_value):
    #     # print((i, key_value[i]), end="")
    #     print(i)
    # for i in key_value:
    #     print(i, key_value[i])


def main():
    dictionairy()


# 主函数
if __name__ == '__main__':
    main()

# sorted() 函数对所有可迭代的对象进行排序操作。
#
# sort 与 sorted 区别：
#
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
#
# list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，
# 而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

# sorted 语法：
#
# sorted(iterable, cmp=None, key=None, reverse=False)

# iterable -- 可迭代对象。
# cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

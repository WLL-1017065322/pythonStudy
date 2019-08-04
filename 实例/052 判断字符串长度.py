# 内置方法len
def judge1(string):
    return len(string)


# 循环计算
def judge2(string):
    count = 0
    while string[count:]:
        count += 1
    return count


string = "runoob"

print(judge1(string))
print(judge2(string))

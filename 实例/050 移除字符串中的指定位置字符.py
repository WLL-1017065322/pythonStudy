def remove_str(str, n):
    new_str = ""
    # print("原始字符串为 : " + test_str)
    for i in range(0, len(str)):
        if (i != n):
            new_str = new_str + str[i]
    return new_str


# replace:
def remove_str1(str, n):
    new_str = str.replace(str[n], "", 1)
    return new_str


# 切片
def remove_str2(str, n):
    return str[0:n] + str[n + 1:]


test_str = "Runoob"
# remove_str(test_str,2)
print(remove_str(test_str, 2))
print(remove_str1(test_str, 2))
print(remove_str2(test_str, 2))

# 使用updata()方法
def Merge(dict1, dict2):
    return (dict2.update(dict1))


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# 返回 None
print(Merge(dict1, dict2))
# dict2 合并了 dict1
print(dict2)

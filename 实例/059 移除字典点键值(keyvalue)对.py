# 使用del 删除
test_dict = {"Runoob" : 1, "Google" : 2, "Taobao" : 3, "Zhihu" : 4}

print("字典移除前:" + str(test_dict))

del test_dict['Zhihu']

print("字典移除后:" + str(test_dict))

# 使用pop()
test_dict1 = {"Runoob" : 1, "Google" : 2, "Taobao" : 3, "Zhihu" : 4}

print("字典移除前:" + str(test_dict1))

removed_value = test_dict1.pop("Zhihu")

print("字典移除后:" + str(test_dict1))
print("移除的值" + str(removed_value))
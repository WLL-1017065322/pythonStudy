# 1.list定义
#
li = ["a","b","mpilgrim","z","example"]
print(li)

# 2.list负数索引
#
print(li[-1])
print(li[0])
print(li[-5])
print(li[1:3])
print(li[0:-2])
# 3.list增加元素
#
print("====3====")
print(li.append("new"))
print(li)
print(li.insert(2,"new"))
print(li)
print(li.extend(["two","element"]))
print(li)


# 4.list搜索
#
print("===4===")
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']

print(li.index("example"))
print(li.index("new"))
# print(li.index("c"))
print("c" in li)

# 5.list删除元素
#
print("==5==")
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
li.remove("a")
print(li)
 # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
liPop=li.pop()
print(liPop)


# 6.list运算符
#
print("===6====")
li = ['a', 'b', 'mpilgrim']
li = li + ['example', 'new']
print(li)
li += ["two"]
print(li)
li = [1, 2] * 3
print(li)

# 7.使用join链接list为字符串
#
print("===7===")
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
params1 = ["%s=%s" %(k,v) for (k,v) in params.items()]
print(params1)
# params2 = ";".join(params1)
params2 = ";".join(["%s=%s" %(k,v) for k,v in params.items()])
print(params2)


# 8.list分割字符串
#
print("===8===")
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print(s)

print(s.split(";"))
print(s.split(";",1))

# 9.list的映射解析
#
print("===9===")
li = [1, 9, 8, 4]
li1 = [elem*2 for elem in li]
print(li1)
print(li)

# 10.dictionary中的解析(字典)
#
print("==10==")

params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(params.keys())
print(params.values())
print(params.items())

print([k for k,v in params.items()])
print([v for k,v in params.items()])


# 11.list过滤
print("====11====")
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
print([elem for elem in li if len(elem)>2])
print([elem for elem in li if li.count(elem) == 2])
#count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
#str.count(sub, start= 0,end=len(string))
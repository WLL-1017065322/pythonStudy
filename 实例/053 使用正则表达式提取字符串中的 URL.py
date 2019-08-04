import re


def find(string):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-f]{2}))+', string)
    return url

# 01?匹配前面的子表达式零次或一次
# 匹配 ?:pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用。
# 这在使用 "或" 字符 (|) 来组合一个模式的各个部分是很有用。
# 例如， 'industr(?:y|ies) 就是一个比 'industry|industries' 更简略的表达式

# 02 ()
# 标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用。要匹配这些字符，请使用 \( 和 \)。

# 03 []

#04 | 	指明两项之间的一个选择。要匹配 |，请使用 \|。

# 05 \w
# 表示匹配数字、字母、下划线和加号本身字符

# #\d 匹配数字

# {n}
# n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。
string = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
print("URLS:", find(string))

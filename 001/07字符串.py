# 字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。
#
# 创建字符串很简单，只要为变量分配一个值即可。例如：
#
# var1 = 'Hello World!'
# var2 = "Runoob"


# Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
#
# Python 访问子字符串，可以使用方括号来截取字符串，如下实例：
#
# var1 = 'Hello World!'
# var2 = "Runoob"
#
# print("var1[0]: ", var1[0])
# print("var2[1:5]: ", var2[1:5])

# 字符串拼接 print ("已更新字符串 : ", var1[:6] + 'Runoob!')

# 转义字符
#
# \(在行尾时)	续行符
# \\	反斜杠符号
# \'	单引号
# \"	双引号
# \a	响铃
# \b	退格(Backspace)
# \000	空
# \n	换行
# \v	纵向制表符
# \t	横向制表符
# \r	回车
# \f	换页
# \oyy	八进制数，yy代表的字符，例如：\o12代表换行
# \xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
# \other	其它的字符以普通格式输出


# 字符串运算符

# +	字符串连接	a + b 输出结果： HelloPython
# *	重复输出字符串	a*2 输出结果：HelloHello
# []	通过索引获取字符串中字符	a[1] 输出结果 e
# [ : ]	截取字符串中的一部分，遵循左闭右开原则，str[0,2] 是不包含第 3 个字符的。	a[1:4] 输出结果 ell
# in	成员运算符 - 如果字符串中包含给定的字符返回 True	'H' in a 输出结果 True
# not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	'M' not in a 输出结果 True
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
# print( r'\n' )
# print( R'\n' )
# %	格式字符串	请看下一节内容。


#字符串格式化

# % c
# 格式化字符及其ASCII码
# % s
# 格式化字符串
# % d
# 格式化整数
# % u
# 格式化无符号整型
# % o
# 格式化无符号八进制数
# % x
# 格式化无符号十六进制数
# % X
# 格式化无符号十六进制数（大写）
# % f
# 格式化浮点数字，可指定小数点后的精度
# % e
# 用科学计数法格式化浮点数
# % E
# 作用同 % e，用科学计数法格式化浮点数
# % g  % f和 % e的简写
# % G  % f 和 % E的简写
# % p
# 用十六进制数格式化变量的地址



# Python三引号
# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符


# Unicode 字符串
# 在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。
#
# 在Python3中，所有的字符串都是Unicode字符串。
#
# Python 的字符串内建函数
# Python 的字符串常用内建函数如下：
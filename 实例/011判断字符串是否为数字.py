

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass


    try:
        ##unicodedata.numeric(chr[, default])
        # 把一个表示数字的字符串转换为浮点数返回。比如可以把‘8’，‘四’转换数值输出。
        # 与digit（）不一样的地方是它可以任意表示数值的字符都可以，不仅仅限于0到9的字符。
        # 如果不是合法字符，会抛出异常ValueError。

        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass

    return False


# 测试字符串和数字
print(is_number('foo'))  # False
print(is_number('1'))  # True
print(is_number('1.3'))  # True
print(is_number('-1.37'))  # True
print(is_number('1e3'))  # True

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四'))  # True
# 版权号
print(is_number('©'))  # False
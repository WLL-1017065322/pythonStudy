def reverse1(str):
    str = str[::-1]
    return str


def reverse2(str):
    # new_str = ''
    new_str = ''.join(reversed(str))
    return new_str


str = 'Runoob'
print(reverse1(str))
print(reverse2(str))

def check(str, sub_str):
    if (str.find(sub_str) == -1):
        print("不存在")
    else:
        print("存在")


str = "www.runoob.com"
sub_str = "runoob"
check(str, sub_str)

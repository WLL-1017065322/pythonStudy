# w, r, wt, rt 都是 python 里面文件操作的模式。
#
# w 是写模式，r 是读模式。
#
# t 是 windows 平台特有的所谓 text mode(文本模式）,区别在于会自动识别 windows 平台的换行符。
#
# 类 Unix 平台的换行符是 \n，而 windows 平台用的是 \r\n 两个 ASCII 字符来表示换行，python 内部采用的是 \n 来表示换行符。
#
# rt 模式下，python 在读取文本时会自动把 \r\n 转换成 \n。
#
# wt 模式下，Python 写文件时会用 \r\n 来表示换行。

# 写文件

with open("test.txt","wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！嘿嘿")


# 读文件

with open("test.txt","rt") as in_file:
    text = in_file.read()

print(text)

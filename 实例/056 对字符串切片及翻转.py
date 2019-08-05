def rotate(input, d):
    Lfirst = input[0:d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]

    print("头部切片翻转 : ", (Lsecond + Lfirst))
    print("尾部切片翻转 : ", (Rsecond + Rfirst))


if __name__ == "__main__":
    input = 'Runoob'
    d = 2  # 截取两个字符
    rotate(input, d)

    # 利用索引进行切片操作时，可包含三个参数:
    #
    # 如对列表来说即：list[start_index: stop_index: step]。
    #
    # 起始位置: start_index(空时默认为
    # 0)。
    # 终点位置: stop_index(空时默认为列表长度)
    # 需要注意起点与终点索引的位置关系。
    # 步长: step(空时默认为
    # 1，不能为
    # 0)。

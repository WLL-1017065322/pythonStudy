# 30 个人在一条船上，超载，需要 15 人下船。
#
# 于是人们排成一队，排队的位置即为他们的编号。
#
# 报数，从 1 开始，数到 9 的人下船。
#
# 如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？

people = {}

for x in range (1,31):
    people[x] = 1

print(people)
i = 1
j = 0
check = 0

while i <=31:
    if i == 31:
        i = 1
    elif j == 15:
        break
    else :
        if people[i] == 0:
            i += 1
            continue
        else:
            check += 1
            if check == 9:
                people[i] = 0
                check = 0
                print("{}号下船了".format(i))
                j += 1
            else:
                i += 1
                continue

####分析：下面的编程思想是，用pop删除第一个数字并添加到最后，循环9次，用pop返回第一个数字
print("=====2====")
people = list(range(1,30))
print(people)
while len(people)>15:
    i = 1
    while i<9:
        people.append(people.pop(0))
        i += 1
    print("{:2d}号下船了".format(people.pop(0)))
    #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    # append() 方法用于在列表末尾添加新的对象。


##### 分析：输出第九个数字，然后将列表前九个数字和剩余颠倒，使用切片
print("===3===")
def main():
    persons = [x for x in range(1,31)]
    #下船人数
    dropped = 0
    while (dropped < 15):
        print("下船的船号是：",persons[8])
        # 对列表进行切片操作，每次截取前9位后的数据和前8位的数据
        persons = persons[9:] + persons[0:8]
        print("截取后的list：",persons)
        dropped += 1

    print("剩余的号数是：")
    print(sorted(persons))

main()


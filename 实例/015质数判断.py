


def is_primeNum(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                return print(num,"不是质数")
                # print("不是质数")
                # break
        # else:
        #     print("质数")

        return print(num,"是质数")
    else:
        print(num,"不是质数")


num = int(input("输入数字"))
is_primeNum(num)
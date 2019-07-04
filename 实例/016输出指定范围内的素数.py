




def outputPrimeNum(min,max):
    for i in range(min,max + 1):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                print(i)

min = int(input("输入最小值"))
max = int(input("输入最大值"))
outputPrimeNum(min,max)
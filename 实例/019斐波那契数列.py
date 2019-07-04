
def FibonacciSequence(n):

    a,b,i =0,1,0

    if n < 0:
        print("没有")
    elif n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    elif n >2:
        print(a, b, end=",")
        while i < n-2:
            sum = a + b
            print(sum,end=",")
            a = b
            b = sum
            i =i + 1


n = int(input("几项？"))
FibonacciSequence(n)
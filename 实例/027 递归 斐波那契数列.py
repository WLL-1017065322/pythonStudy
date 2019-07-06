

def reur_fibo(n):
    if n <= 1:
        return n
    else:
        return reur_fibo(n-1)+reur_fibo(n-2)

nterms = int(input("几项？"))

if nterms < 0:
    print("请输入正数")
else:
    for i in range(nterms):
        print(reur_fibo(i))

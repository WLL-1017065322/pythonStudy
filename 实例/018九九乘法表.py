
def paint(a):
    for i in range(1,a+1):
        for j in range(1,i+1):
            print("{}x{}={}\t".format(j,i,i*j),end='')
        print()

paint(9)
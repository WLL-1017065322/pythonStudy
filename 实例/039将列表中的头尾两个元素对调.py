def touweiduidiao(arr):
    arr[0],arr[-1]=arr[-1],arr[0]
    return arr

arr = [1,2,3,4,5,6]

print(touweiduidiao(arr))
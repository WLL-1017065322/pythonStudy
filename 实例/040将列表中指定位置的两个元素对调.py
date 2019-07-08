def duidiaozhiding(arr,a,b):
    arr[a],arr[b] = arr[b],arr[a]
    return arr


arr = [1,2,3,4,5,6]


print(duidiaozhiding(arr,1,2))
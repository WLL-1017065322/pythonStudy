

# def leftRotate(arr,d,n):
#     for i in range(d):
#         leftRotateByOne(arr,n)
#
# def leftRotateByOne(arr,n):
#     temp = arr[0]
#     for i in range(n-1):
#         arr[i] = arr[i+1]
#     arr[n-1] = temp
#
# def printArray(arr,size):
#     for i in range(size):
#         print("%d"% arr[i],end="")
#
#
# arr = [1, 2, 3, 4, 5, 6, 7]
# leftRotate(arr,2,7)
# printArray(arr,7)

def fanzhuan(arr,d):
    n = len(arr)
    arr = arr[d:] + arr[:d]
    return arr
arr = [1,2,3,4,5,6,7]
print("翻转前:",arr)
print("翻转后",fanzhuan(arr,2))

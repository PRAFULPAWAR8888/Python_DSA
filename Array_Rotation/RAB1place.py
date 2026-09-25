
arr = [1,2,3]
def rotation(arr):
    n = len(arr)
    temp = arr[n-1]

    for i in range(n-2,-1,-1):
        arr[i + 1] = arr[i]

    arr[0] = temp

    return arr

print(rotation([2,4,4,5]))


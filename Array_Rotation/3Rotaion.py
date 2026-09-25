arr = [1,2,3,4]

def r3(arr,k):
    n = len(arr)

    for _ in range(k):
        temp = arr[n-1]
        for i in range(n-2,-1,-1):
            arr[i + 1] = arr[i]

        arr[0] = temp
 
    return arr

print(r3([3,2,47,6,9],3))

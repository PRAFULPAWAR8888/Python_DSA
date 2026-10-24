def sort(arr):
    n  = len(arr)
    temp = None
    for i in range(0,n-1):
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
    return arr



def merge_unique_sorted(arr1, arr2):
    a, b = sorted(arr1), sorted(arr2)   # replace with your own sort if not allowed
    result = []
    i = j = 0

    while i < len(a) or j < len(b):
        if j >= len(b) or (i < len(a) and a[i] <= b[j]):
            val = a[i]
            i += 1
        else:
            val = b[j]
            j += 1

        if not result or result[-1] != val:
            result.append(val)

    return result

print(merge_unique_sorted([1,2,3,4,5],[1,3,4,5,9,8]))

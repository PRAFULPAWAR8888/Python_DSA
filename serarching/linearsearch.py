# arr = [2,5,9,8,9]
# target = 9
# found = False
# n = len(arr)
# for i in range(0 , n):
#     if target == arr[i]:
#         print(i)
#         found = True

# if not found:
#     print(-1)

def linear_search(arr,target):
    n = len(arr)
    found = False
    for i in range(0 , n):
        if target == arr[i]:
            return i
            

    return  -1

obj = linear_search
print(obj([1,24,3,4,5],3))


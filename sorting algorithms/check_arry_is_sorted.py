# def sorted_arr(arr):
    
#     n = len(arr)
#     for i in range(n):
#         for j in range(i+1,n):
#             if arr[i] > arr[j]:
#                 arr[i],arr[j] = arr[j], arr[i]


#     return arr



# print(sorted_arr([2,3,1,23,12,9,18]))


def check_arr(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                return False
    
    return True
           
           
print(check_arr([1,2,3]))
            
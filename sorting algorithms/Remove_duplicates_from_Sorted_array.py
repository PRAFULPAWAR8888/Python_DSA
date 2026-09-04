
def remove_duplicate(arr):
    n = len(arr)
    for i in range( n - 1):
        for j in range(i + 1, n):

            if arr[i]> arr[j]:
                arr[i], arr[j] = arr[j],arr[i]


    freq_map = {}

    for i in range(n):
        freq_map[arr[i]] = 0

    j = 0
    for k in freq_map:
        arr[j] = k
        j += 1

    return(arr,j)



print(remove_duplicate([3,42,2,1,1,2,3]))


# def removeDuplicates(nums) -> int:
#       j = 1

#       for i in range(1, len(nums)):
#         if nums[i]  != nums[i -1]:
#             nums[j] = nums[i]
#             j += 1
    
#       return j
# print(removeDuplicates([3,42,2,1,1,2,3]))
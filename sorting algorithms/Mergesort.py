
def merge_array(left, right):
    result = []
    i = j = 0
    n, m = len(left), len(right)
    
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
        
    
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1
            
    return result

# print(merge_array([1,3,5,7,9], [2,4,6,8,10]))


def merge_sort(nums):
    
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_arr = merge_sort(nums[:mid])
    right_arr = merge_sort(nums[mid:])
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_array(left, right)

print(merge_sort([3,3,53,6,44,54,224,1,3,1,2,34,2]))
  
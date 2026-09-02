
  
def merge_array(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)

    while i < n and j < m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < n:
        result.append(left[i])
        i += 1

    while j < m:
        result.append(right[j])
        j += 1

    return result
    
def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums

    mid = n // 2
    left_f = nums[:mid]
    right_r = nums[mid:]
    left = merge_sort(left_f)
    right = merge_sort(right_r)
    return merge_array(left, right)

print(merge_sort([3,3,53,6,44,54,224,1,3,1,2,34,2]))
         
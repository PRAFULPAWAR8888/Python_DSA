nums = [ 1,3,2,6,7,10, 11]
def  insertion_sort(nums):
    n = len(nums)

    for i in range(1,n):
        key = nums[i]
        j = i - 1
    
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        
        nums[j + 1] = key  

    return nums

print(insertion_sort([3,3,53,6,44,54,224,1,3,1,2,34,2]))

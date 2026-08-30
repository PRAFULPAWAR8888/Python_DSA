
def b_sort(nums):
    
    n = len(nums)
    
    for i in range( n):
        for j in range(n -i -1): 
          if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    
    return nums  

print(b_sort([1,2,34,2,1]))




    




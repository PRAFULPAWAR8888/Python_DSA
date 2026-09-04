def second_largest(nums):
    first_largest = nums[0]
    second_largest = nums[1]

    for i in range(2, len(nums)):
        if nums[i] > first_largest:
           second_largest = first_largest
           first_largest = nums[i]

        elif nums[i] > second_largest:
            second_largest = nums[i]
           
           
           
    return second_largest
print(second_largest([1,2,42,13]))
 
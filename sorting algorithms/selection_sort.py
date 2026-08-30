def selection_sort(nums):
    n = len(nums)
    i = 0

    while i < n:
        min_ind = i
        j = i + 1

        while j < n:
            if nums[j] < nums[min_ind]:
                min_ind = j

            j += 1

        nums[i], nums[min_ind] = nums[min_ind], nums[i]

        i += 1

    return nums


print(selection_sort([2, 34, 3, 532, 2, 23]))
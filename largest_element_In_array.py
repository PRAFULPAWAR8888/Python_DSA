
def largest_element(arr):

    if not arr:
        return "arr not inserted"
    largest = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest

print(largest_element([2,3,41,313,42]))

             
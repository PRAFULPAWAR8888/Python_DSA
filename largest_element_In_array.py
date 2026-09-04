
def largest_element(arr):

    if not arr:
        return "arr not inserted"
    largest = None
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                largest = arr[j]

    return largest

print(largest_element([2,3,41,313,42]))

             
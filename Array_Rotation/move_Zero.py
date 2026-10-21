
arr = [1,0,9,8,0,0,3]

n = len(arr)
temp = []

for i in range(0 , n):
    if arr[i] != 0:
        temp.append(arr[i])

nz = len(temp)
for i in range(0,nz):
    arr[i] = temp[i]
for i in range(nz,n):
    arr[i] = 0


print(arr)

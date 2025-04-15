n = int(input())
arr = list(map(int, input().split()))

sort = False


for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            
for i in arr:
    print(i, end=" ")
# Please write your code here.

n = int(input())
arr = list(map(int, input().split()))

for i in range(1,n):
    j = i -1
    temp = arr[i]
    while(j >=0 and arr[j] > temp):
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = temp
for i in arr:
    print(i, end = " ")
# Please write your code here.

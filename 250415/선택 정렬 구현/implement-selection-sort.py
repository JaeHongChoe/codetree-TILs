n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    minn = i
    for k in range(minn,n-1):
        if arr[k] < arr[minn]:
            minn = k
    tmp = arr[i]
    arr[i] = arr[minn]
    arr[minn] = tmp

for i in arr:
    print(i, end= " ")

# Please write your code here.

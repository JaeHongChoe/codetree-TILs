n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

for i in range(m):
    left, right = 0, n-1
    min_idx = 9999999999
    while left <= right:
        mid = (left+right) //2
        if arr[mid] < query[i]:
            left = mid +1
        else:
            right = mid -1
        if arr[mid] == query[i]:
            min_idx = min(min_idx,mid)+1
    if min_idx != 9999999999:
        print(min_idx)
    else:
        print(-1)
# Please write your code here.

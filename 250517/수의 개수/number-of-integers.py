n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

for i in range(m):
    left , right = 0, n-1
    min_idx, max_idx = n,n
    while left <= right:
        mid = (left + right) //2
        if arr[mid] <= queries[i]:
            left = mid + 1
        else:
            max_idx = min(max_idx,mid)
            right = mid - 1

    left , right = 0, n-1
    while left <= right:
        mid = (left + right) //2
        if arr[mid] < queries[i]:
            left = mid + 1
        else:
            min_idx = min(min_idx,mid)
            right = mid - 1
    # print(max_idx , min_idx)
    print(max_idx - min_idx)

# Please write your code here.

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

for i in range(m):
    left, right = 0 , n -1
    while True:
        mid = (left + right) //2
        if arr[mid] == queries[i]:
            print(mid+1)
            break
        elif left >= right:
            print(-1)
            break
        if arr[mid] > queries[i]:
            right = mid -1
        else:
            left = mid + 1
# Please write your code here.

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(n-k+1):
    if ans < sum(arr[i:i+k]):
        ans = sum(arr[i:i+k])
print(ans)
# Please write your code here.
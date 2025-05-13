N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 99999999
temp = sum(arr)
for i in range(N):
    for k in range(i+1, N):
        l = abs(temp - arr[i] - arr[k] - S)
        if ans > l:
            ans = l
print(ans)
    
# Please write your code here.
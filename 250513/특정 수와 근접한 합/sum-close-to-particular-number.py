N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 99999999
temp = sum(arr)
for i in range(N):
    for k in range(i+1, N):
        if ans > temp - arr[i] - arr[k] - S:
            ans = temp - arr[i] - arr[k] - S 
print(ans)
    
# Please write your code here.
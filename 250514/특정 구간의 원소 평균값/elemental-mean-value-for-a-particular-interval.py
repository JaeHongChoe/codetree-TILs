n = int(input())
arr = list(map(float, input().split()))
ans = 0

for k in range(2,n+1):
    for i in range(n-k+1):
        if sum(arr[i:i+k])/k in arr[i:i+k]:
            ans +=1
print(ans+n)
# Please write your code here.
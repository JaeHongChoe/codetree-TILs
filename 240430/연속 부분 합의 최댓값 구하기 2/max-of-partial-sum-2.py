a = int(input())
b = list(map(int,input().split()))
ans =-9999999
temp =0
for k in range(a):
    if temp < b[k] and temp <0:
        temp =0

    temp += b[k]
    ans = max(ans,temp)
    

print(ans)
a = int(input())
b = list(map(int,input().split()))
ans =-9999999

for k in range(a):
    temp =0
    for n in range(k+1,a):
        temp += b[n]
        ans = max(ans,temp)

print(ans)
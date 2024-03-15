n,m = map(int,input().split())
ans =0
for k in range(n,m+1):
    if k %2 !=0 and k %3 !=0:
        ans+=k
print(ans)
n= list(map(int,input().split()))
ans =0

if len(n) <2:
    print(ans)
    exit(0)

for k in range(n[0],n[1]+1):
    if k %2 !=0 and k %3 !=0:
        ans+=k
print(ans)
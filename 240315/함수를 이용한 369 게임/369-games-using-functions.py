n,m = map(int,input().split())
ans =0
for k in range(n,m+1):
    if k %3 ==0 or k%10 in [3,6,9] or k//10 in[3,6,9]:
        ans +=1
print(ans)
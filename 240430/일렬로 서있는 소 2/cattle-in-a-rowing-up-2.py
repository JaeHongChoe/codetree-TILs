a = int(input())
b= list(map(int,input().split()))
ans =0
for k in range(a):
    left = b[k]
    cent =b[k]
    right = b[k]
    check =0
    for n in b[k+1:]:
        if left <= n and check ==0:
            cent = n
            check =1
        elif cent <=n:
            ans+=1
            break

print(ans)
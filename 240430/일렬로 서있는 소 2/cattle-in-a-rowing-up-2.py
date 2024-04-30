a = int(input())
b= list(map(int,input().split()))
ans =0
for k in range(a):
    left = b[k]
    for n in range(k+1,a):
        if left <= b[n]:
            cent = b[n]
            for right in range(n+1, a):
                if cent <= b[right]:
                    ans+=1

print(ans)
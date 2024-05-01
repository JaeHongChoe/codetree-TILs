n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = list(map(int,input().split()))

a_b ={}
c_d ={}
ans=0

for k in range(n):
    for j in range(n):
        if a[k]+b[j] not in a_b:
            a_b[a[k]+b[j]] =0
        
        if c[k]+d[j] not in c_d:
            c_d[c[k]+d[j]] =0
        
        a_b[a[k]+b[j]] +=1
        c_d[c[k]+d[j]] +=1

for k in a_b:
    if (k*-1) in c_d:
        ans += 1

print(ans)
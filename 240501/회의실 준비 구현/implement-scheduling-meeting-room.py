a = int(input())
b = [ 
    list(map(int,input().split()))
    for _ in range (a)
]

b.sort(key = lambda x:x[1])

cnt=1
check = b[0][1]
for k in range(1,a):
    if check <= b[k][0]:
        cnt+=1
        check = b[k][1]

print(cnt)
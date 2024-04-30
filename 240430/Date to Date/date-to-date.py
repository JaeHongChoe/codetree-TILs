a= list(map(int,input().split()))
total=0
for k in range(a[0],a[2]):
    if k ==2: #28
        total += 28 
    elif k % 2==0: #30
        total += 30
    else: #31
        total += 31


print(total - a[1] + a[3])
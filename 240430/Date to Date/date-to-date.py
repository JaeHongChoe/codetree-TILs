a= list(map(int,input().split()))
total=  a[3]- a[1] +1
for k in range(a[0],a[2]):
    if k ==2: #28
        total += 28 
    elif k in [2,4,6,9,11]: #30
        total += 30
    else: #31
        total += 31

# if total ==0:
#     total+=1
print(total)
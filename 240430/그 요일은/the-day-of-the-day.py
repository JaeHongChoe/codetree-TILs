a = list(map(int,input().split()))
b = input()

ans =['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

total =  a[3] -a[1]

for k in range(a[0],a[2]):
    if k ==2:
        total+=29
    elif k in [4,6,9,11]:
        total +=30
    else:
        total+=31

if ans.index(b) <= total%7:
    total = (total//7)+1
else:
    total = (total//7)
print(total)
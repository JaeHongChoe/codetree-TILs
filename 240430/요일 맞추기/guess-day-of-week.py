a = list(map(int,input().split()))
ans = [ 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun' ]
if a[0] >= a[2] and a[1] <= a[3]:
    left_mon = a[0]
    left_date = a[1]
    right_mon = a[2]
    right_data = a[3]
    check=0
else:
    left_mon = a[2]
    left_date = a[3]
    right_mon = a[0]
    right_data = a[1]
    check=1
    
total = right_data - left_date 

for k in range(left_mon, right_mon):
    if k ==2:
        total += 28
    elif k in [2,4,6,9,11]:
        total += 30
    else:
        total +=31

if check ==0:
    print(ans[total%7])
else:
    print(ans[(total%7)*-1])
    

# print(a[1]-a[3] % 7)
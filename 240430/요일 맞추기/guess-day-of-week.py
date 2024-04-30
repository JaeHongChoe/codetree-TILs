a = list(map(int,input().split()))
ans = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat' ]
if a[0] > a[2]:
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
    ans.reverse()

total = left_date - right_data

for k in range(left_mon, right_mon):
    if k ==2:
        total += 28
    elif k in [2,4,6,9,11]:
        total += 30
    else:
        total +=31

print(ans[total%7])
    

# print(a[1]-a[3] % 7)
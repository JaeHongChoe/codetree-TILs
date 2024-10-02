a = input()

d = [(1,0),(0,1),(-1,0),(0,-1)]
d_dist =0
ans =0
trigger =0
x = 0
y = 0
for i in range(len(a)):
    if a[i] == 'F':
        y = y + d[d_dist][0]
        x = x + d[d_dist][1]
        ans +=1
    elif a[i] == "R":
        d_dist = (d_dist+1)%4
        ans +=1
    if x ==0 and y == 0:
        trigger =1
        break
if trigger:
    print(ans)
else:
    print(-1)
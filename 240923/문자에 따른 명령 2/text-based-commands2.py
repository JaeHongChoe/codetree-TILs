a = input()

#서남동북
d = [(0,-1),(-1,0),(0,1),(1,0)]
x,y=0,0
d_idx=3
check=0

for i in range(len(a)):
    if a[i] =="L":
        d_idx +=1
    elif a[i] == "R":
        d_idx -= 1
    else:
        d_idx = d_idx%4
        check =1

if not check:
    print(0,0)
else:
    x= x+d[d_idx][1]
    y= y+d[d_idx][0]
    print(x,y)
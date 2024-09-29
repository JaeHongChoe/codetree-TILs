a,b = list(map(int,input().split()))
init_y,init_x, dirt = list(map(str,input().split()))

d = [(-1,0),(0,1),(1,0),(0,-1)]

def in_range(x,y):
    return 1 <= x and x < a-1 and 1<=y and y <a-1

#Up, Down, Right, Left
d_dir = {'U':0,
        'R':1,
        'D':2,
        'L':3
        }
dd = d_dir[dirt]
x = int(init_x)
y = int(init_y)
turn = 0
for i in range(b):

    ny,nx = y + d[d_dir[dirt]][0], x+d[d_dir[dirt]][1]
    if not in_range(nx,ny)and turn ==0:
        if dd == 0:
            dd = 2
        elif dd == 1:
            dd = 3
        elif dd == 2:
            dd = 0
        else:
            dd = 1
        turn =1
    else:
        y,x = y + d[dd][0], x+d[dd][1]
        turn =0

print(y,x)
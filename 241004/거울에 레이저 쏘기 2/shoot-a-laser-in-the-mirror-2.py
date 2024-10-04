n = int(input())

grid =[
    list(map(str,input().split()))
    for _ in range(n)
]

start = int(input())

d = [(1,0),(0,-1),(-1,0),(0,1)]
trig = 1
cnt =1
if start <=n:
    d_dist =0
    x, y = start-1,0
elif start <= n*2:
    d_dist = 1
    x, y = n-1, start - n - 1
elif start <= n*3:
    d_dist = 2
    x, y = n - (start - n*2), n-1
else:
    d_dist = 3
    x, y = 0, n - (start - n*3)

def in_range(x,y):
    return 0 <= x and 0 <= y and x < n and y < n

while(trig):
    # print(y,x)
    block = grid[y][0][x]
    # print(block)
    if block == "\\":
        if d_dist ==0:
            d_dist = 3
        elif d_dist == 1:
            d_dist = 2
        elif d_dist == 2:
            d_dist = 1
        else:
            d_dist = 0
    elif block == "/":
        if d_dist ==0:
            d_dist = 1
        elif d_dist == 1:
            d_dist = 0
        elif d_dist == 2:
            d_dist = 3
        else:
            d_dist = 2
    ny , nx = y + d[d_dist][0], x + d[d_dist][1]
    # print(ny,nx)
    if not in_range(nx,ny):
        trig = 0
    else:
        cnt +=1
        y = ny
        x = nx

print(cnt)
# print(grid[1][0][2])
# print(n,grid,start)
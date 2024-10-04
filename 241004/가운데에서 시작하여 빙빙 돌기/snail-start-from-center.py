n = int(input())
grid = [[0]*n for _ in range(n)]

x = n//2
y = n//2

cnt =1
d = [(0,1),(-1,0),(0,-1),(1,0)]
d_dist = 0
work = 1
step = 0
count_step=0
grid[y][x] = cnt
trig = 1

def in_range(x,y):
    return 0 <= x and 0 <= y and x <n and y<n

while(trig):
    for _ in range(work):
        ny, nx = y + d[d_dist][0],x + d[d_dist][1]
        if not in_range(nx,ny):
            trig = 0
            break
        cnt +=1
        grid[ny][nx] = cnt
        x = nx
        y = ny
    d_dist = (d_dist+1)%4
    step +=1

    if step ==2:
        step =0
        work+=1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = " ")
    print()
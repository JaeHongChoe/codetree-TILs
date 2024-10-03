n,m = list(map(int,input().split()))

grid = [[0]*m for _ in range(n)]
d = [(1,0),(0,1),(-1,0),(0,-1)]
def in_range(x,y):
    return 0 <= x and 0<=y and x < m and y < n

d_dist =0
x = 0 
y = 0
cnt = 1
grid[y][x] = cnt
for _ in range(1, n*m):
    ny, nx = y + d[d_dist][0], x + d[d_dist][1]
    if in_range(nx,ny) and grid[ny][nx] == 0 :
        y = ny
        x = nx
    else:
        d_dist = (d_dist+1)%4
        ny, nx = y + d[d_dist][0], x + d[d_dist][1]
        y = ny
        x = nx
    cnt +=1
    grid[y][x] = cnt

for i in range(n):
    for j in range(m):
        print(grid[i][j], end = " ")
    print()
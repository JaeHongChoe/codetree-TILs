n,m = list(map(int,input().split()))

grid = [[0]*m for _ in range(n)]
cnt = 1
d = [(0,1),(1,0), (0,-1),(-1,0)]
dirt =0
x=0
y=0
grid[y][x] =cnt
def in_range(x,y):
    return 0 <=x and x < m and y < n and 0<=y

for i in range(2, n*m+1):
    ny, nx = y + d[dirt][0], x + d[dirt][1]
    if not in_range(nx,ny) or grid[ny][nx] !=0:
        dirt = (dirt+1)%4
    y,x = y + d[dirt][0], x + d[dirt][1]
    # print(y,x,dirt,grid)
    cnt +=1
    grid[y][x] = cnt
        


for i in range(n):
    for j in range(m):
        print(grid[i][j], end = " ")
    print()
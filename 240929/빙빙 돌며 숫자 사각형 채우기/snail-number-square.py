n,m = list(map(int,input().split()))

grid = [[0]*n for _ in range(m)]
cnt = 1
d = [(0,1),(1,0), (0,-1),(-1,0)]
dirt =0
x=0
y=0
def in_range(x,y):
    return 0 <=x and x < n and y < m and 0<=y

for i in range(n):
    for j in range(m):
        grid[y][x] = cnt
        cnt +=1
        ny, nx = y + d[dirt][0], x + d[dirt][1]
        if not in_range(nx,ny) or grid[ny][nx] !=0:
            dirt = (dirt+1)%4
        y,x = y + d[dirt][0], x + d[dirt][1]

for i in range(n):
    for j in range(m):
        print(grid[i][j], end = " ")
    print()
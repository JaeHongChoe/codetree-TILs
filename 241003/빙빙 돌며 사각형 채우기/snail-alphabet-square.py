n, m = list(map(int,input().split()))

grid = [[0]*m for _ in range(n)]

alpa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'
,'Q','R','S','T','U','V','W','X','Y','Z']

d = [(0,1),(1,0),(0,-1),(-1,0)]
d_dist = 0
x, y = 0,0
cnt =0
grid[y][x] = alpa[cnt]

def in_range(x,y):
    return 0 <= x and  0<=y and x < m and y < n

for _ in range(1,n*m):
    ny , nx = y + d[d_dist][0], x + d[d_dist][1] 
    if not in_range(nx,ny) or grid[ny][nx] !=0:
        d_dist = (d_dist+1)%4
        ny , nx = y + d[d_dist][0], x + d[d_dist][1]

    if cnt == 26:
        cnt = -1
    cnt +=1
    grid[ny][nx] = alpa[cnt]
    x = nx
    y = ny

for i in range(n):
    for j in range(m):
        print(grid[i][j], end = " ")
    print()
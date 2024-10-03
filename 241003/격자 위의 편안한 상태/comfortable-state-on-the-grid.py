g, count = list(map(int,input().split()))
grid = [[0]*g for _ in range(g)]
kk = [
    list(map(int,input().split()))
    for _ in range(count)
]

d = [(-1,0),(0,1),(1,0),(0,-1)]

def in_range(x,y):
    return 0 <= x and x < g and 0 <= y and y < g

for i in range(count):
    x = kk[i][1]-1
    y = kk[i][0]-1
    grid[y][x] = 1
    ans = 0
    for j in range(4):
        nx , ny = x + d[j][1], y +d[j][0]
        if in_range(nx,ny):
            if grid[ny][nx] ==1:
                ans +=1
    if ans ==3:
        print(1)
    else:
        print(0)
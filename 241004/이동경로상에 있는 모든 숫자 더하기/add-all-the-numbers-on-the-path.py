n, count = list(map(int,input().split()))

command = input()

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]
x = n//2
y = n//2

d = [(-1,0),(0,1),(1,0),(0,-1)]
d_dist = 0

ans = grid[y][x]
def in_ragne(x,y):
    return 0 <= x and 0 <= y and x < n and y < n

for i in range(count):
    if command[i] == "R":
        d_dist = (d_dist+1)%4
    elif command[i] == "L":
        d_dist = (d_dist-1)%4
    else:
        ny, nx = y + d[d_dist][0], x + d[d_dist][1]
        if in_ragne(nx,ny):
            ans += grid[ny][nx]
            y = ny
            x = nx
print(ans)
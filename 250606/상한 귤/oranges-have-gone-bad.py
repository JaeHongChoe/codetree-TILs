n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
arr = []
for i in range(n):
    for j in range(n):
        if grid[i][j]==2:
            arr.append((i,j))

def in_range(y,x):
    return x >=0 and x <=n-1 and y >=0 and y <=n-1

def push(y,x,s):
    visited[y][x]=s

def bfs():
    global visited
    d = [(0,-1),(1,0),(0,1),(-1,0)]
    while q:
        y,x = q.popleft()
        for loc in range(len(d)):
            dy, dx = d[loc]
            oy, ox = dy+y, dx+x
            if in_range(oy,ox) and grid[oy][ox]==1 and (visited[oy][ox] == 0 or visited[y][x]+1 < visited[oy][ox]):
                push(oy,ox,visited[y][x]+1)
                q.append((oy,ox))
    # print(visited)


from collections import deque


for i in arr:
    q = deque()
    q.append(i)
    visited[i[0]][i[1]] = 0
    bfs()
for i in range(n):
    for j in range(n):
        if grid[i][j] ==0:
            print(-1, end=" ")
        elif grid[i][j] == 1 and visited[i][j] ==0:
            print(-2, end=" ")
        else:
            print(visited[i][j],end=" ")
    print()

# Please write your code here.

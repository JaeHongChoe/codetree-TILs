n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]
from collections import deque

q= deque()

def in_range(y,x):
    return x >= 0 and x <= n-1 and y >=0 and y <= n-1

def bfs():
    d = [(0,-1),(1,0),(0,1),(-1,0)]
    for loc in points:
        q.append((loc[0]-1,loc[1]-1))
        visited = [[0]*n for _ in range(n)]
        visited[loc[0]-1][loc[1]-1] = 1
        ans =1
    while q:
        y,x = q.popleft()
        for i in range(len(d)):
            dy, dx = d[i]
            oy, ox = dy+y , dx+x
            if in_range(oy,ox) and grid[oy][ox] != 1 and visited[oy][ox] ==0:
                if grid[oy][ox] ==0:
                    ans +=1
                visited[oy][ox] = 1
                grid[oy][ox] = 2
                q.append((oy,ox))
    return ans

print(bfs())

# Please write your code here.

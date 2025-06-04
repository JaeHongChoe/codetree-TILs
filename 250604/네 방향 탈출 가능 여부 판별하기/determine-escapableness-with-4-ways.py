n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
from collections import deque
q = deque()

def in_range(y,x):
    return x >= 0 and x <= m-1 and y >= 0 and y <= n-1

def bfs():
    d = [(0,-1),(1,0),(0,1),(-1,0)]
    while q:
        y,x = q.popleft()
        if (y,x) == (n-1,m-1):
            return 1
        for i in range(len(d)):
            dy, dx = d[i]
            oy, ox = dy +y , dx + x
            if in_range(oy,ox) and visited[oy][ox] == 0 and a[oy][ox] == 1:
                q.append((oy,ox))
                visited[oy][ox] = 1
    return 0
    # print(visited)
q.append((0,0))
visited[0][0] = 1
print(bfs())
# Please write your code here.

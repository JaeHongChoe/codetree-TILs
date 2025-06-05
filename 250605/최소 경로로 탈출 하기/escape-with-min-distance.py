n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(m)]

def in_range(y,x):
    return x >=0 and x <=n-1 and y >=0 and y <= m-1

def push(y,x,s):
    visited[y][x] = s

def bfs():
    global visited
    d = [(0,-1),(1,0),(0,1),(-1,0)]
    cnt=1
    while q:
        y,x = q.popleft()
        cnt+=1
        for i in range(len(d)):
            dy, dx = d[i]
            oy, ox = dy+y, dx+x
            if in_range(oy,ox) and visited[oy][ox] == 0 and a[oy][ox]==1:
                push(oy,ox,visited[y][x]+1)
                q.append((oy,ox))

from collections import deque
q = deque()
q.append((0,0))
visited[0][0] = 1

bfs()
print(visited[-1][-1]-1)

# Please write your code here.

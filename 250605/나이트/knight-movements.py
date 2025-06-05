n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[0]*n for _ in range(n)]
def in_range(y,x):
    return x >=0 and x <=n-1 and y >=0 and y <=n-1

def push(y,x,s):
    visited[y][x]=s
def bfs():
    d=[(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]
    while q:
        y,x = q.popleft()
        if (y,x) == (r2-1,c2-1):
            # print(visited)
            print(y,x)
            return visited[y][x]
        for i in range(len(d)):
            dy, dx = d[i]
            oy, ox = dy+y, dx+x
            if in_range(oy,ox) and visited[oy][ox] == 0:
                push(oy,ox,visited[y][x]+1)
                q.append((oy,ox))
    # print(visited)
    return -1

from collections import deque
q = deque()
q.append((r1-1,c1-1))
print(bfs())
# Please write your code here.

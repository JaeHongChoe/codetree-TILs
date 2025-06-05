n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = []
from collections import deque
def in_range(y,x):
    return x >= 0 and x <= m-1 and y >=0 and y <= n-1

def bfs():
    d = [(0,-1),(1,0),(0,1),(-1,0)]
    total = 0
    q.append((0,0))
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(len(d)):
            dy, dx = d[i]
            oy, ox = y+dy, x+dx
            if in_range(oy,ox) and visited[oy][ox] == 0 and a[oy][ox]==0:
                visited[oy][ox] = 1
                q.append((oy,ox))
                cnt+=1
            if in_range(oy,ox) and a[y][x] == 0 and a[oy][ox] ==1:
                a[oy][ox] = 0
                visited[oy][ox] = 1
                total += 1
                cnt+=1
    return total, cnt

q = deque()
returnn = []
while True:
    ans,cnt = bfs()
    if ans != 0:
        returnn.append(ans)
    if cnt == n*m:
        break
if len(returnn) !=0:
    print(len(returnn), returnn[-1])
else:
    print(1,0)

# Please write your code here.

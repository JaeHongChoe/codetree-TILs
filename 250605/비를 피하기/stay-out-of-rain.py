n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# visited = [[0]*n for _ in range(n)]

def in_range(y,x):
    return x >=0 and x <= n-1 and y >=0 and y<=n-1

def push(my,mx,s):
    # global visited
    visited[my][mx] = s

def bfs(ori_y,ori_x):
    # global visited
    d = [(0,-1),(1,0),(0,1),(-1,0)]
    visited[ori_y][ori_x]=1
    q.append((ori_y,ori_x))
    # print("start", visited,q)
    while q:
        y, x = q.popleft()
        for loc in range(len(d)):
            dy, dx = d[loc]
            oy, ox = dy+y, dx+x
            if in_range(oy,ox) and visited[oy][ox] ==0 and grid[oy][ox] != 1:
                push(oy,ox,visited[y][x]+1)
                q.append((oy,ox))
                # print(y,x,dy,dx,oy,ox,visited,y,x)
        if grid[y][x] == 3:
            # print()
            # print(oy,ox,y,x,visited[y][x]-1)
            # print(visited)
            # print()
            return visited[y][x]-1
                # print(visited)
    return -1

temp = 0
from collections import deque

for i in range(n):
    for k in range(n):
        temp=0
        if grid[i][k] == 2:
            q=deque()
            visited = [[0]*n for _ in range(n)]
            # cnt+=1
            temp = bfs(i,k)
            # print(visited)
            
        print(temp,end=" ")
    print()
# Please write your code here.

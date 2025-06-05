n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
# ###
# n=100
# grid = [[0]*n for _ in range(n)]
# r2,c2 = 100,100
# ###
visited = [[0]*n for _ in range(n)]
arr = []
rocks = []
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            arr.append([i,j])

rocks.append([r1,c1])
def fac(k,new_arr,c):
    global rocks
    if len(new_arr)==k:
        rocks.append(new_arr)
        return
    for i in range(c,len(arr)):
        fac(k,new_arr+[arr[i]],i+1)
fac(k,[],0)

def in_range(y,x):
    return x >=0 and x <=n-1 and y >=0 and y <=n-1

def push(y,x,s):
    visited[y][x]=s

def bfs():
    global visited
    d = [(0,-1),(1,0),(0,1),(-1,0)]
    ans = 9999999
    for rock in rocks:
        visited = [[0]*n for _ in range(n)]
        visited[r1][c1] = 1
        q=deque()
        q.append((r1,c1))
        while q:
            y,x = q.popleft()
            for loc in range(len(d)):
                dy, dx = d[loc]
                oy, ox = dy+y, dx+x
                if in_range(oy,ox) and visited[oy][ox] ==0 and (grid[oy][ox] !=1 or [oy,ox] in rock):
                    push(oy,ox,visited[y][x]+1)
                    q.append((oy,ox))
                    if (oy,ox) == (r2,c2):
                        ans = min(ans,visited[oy][ox]-1)
                        q=deque()
                        break
        # print(visited)
    if ans == 9999999:
        print(-1)
    else:
        print(ans)
from collections import deque
bfs()

# Please write your code here.

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
from collections import deque
visited = [[0]*n for _ in range(n)]

def in_range(y,x):
    return x >=0 and x <= n-1 and y >= 0 and y <= n-1

def bfs():
    global visited
    d= [(0,-1),(1,0),(0,1),(-1,0)]
    ans = (r,c)
    for _ in range(k):
        # if not q:
        #     return ans
        max_loc = (-1,1,1)
        # visited = [[0]*n for _ in range(n)]
        # visited[r-1][c-1] = 1
        while q:
            # max_loc = (-1,1,1)
            l,y,x = q.popleft()
            for i in range(len(d)):
                dy, dx = d[i][0]+y, d[i][1]+x
                if in_range(dy,dx) and visited[dy][dx] == 0 and grid[dy][dx] < target:
                    visited[dy][dx] = 1
                    q.append((grid[dy][dx],dy,dx))
                    temp_loc = (grid[dy][dx],dy*-1,dx*-1)
                    if max_loc < temp_loc:
                        max_loc = temp_loc
        # print(max_loc)
        # print(visited)
        if max_loc == (-1,1,1):
            return ans 
        else:
            # print(max_loc[1]*-1, max_loc[2]*-1)
            my, mx = max_loc[1]*-1, max_loc[2]*-1
            visited = find_loc(max_loc[0])
            q.append((max_loc[0],my,mx))
            ans = (my+1,mx+1)
        # print(visited)

    return ans
def find_loc(loc):
    best = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if loc <= grid[i][k]:
                visited[i][k] = 1
            if loc == grid[i][k] and best==0:
                best=1
                best_y, best_x = i,k
                # print(i,k)
    return visited

q= deque()
q.append((grid[r-1][c-1],(r-1),(c-1)))
visited[r-1][c-1] = 1
target = grid[r-1][c-1]
a = bfs()
print(a[0],a[1])
# Please write your code here.

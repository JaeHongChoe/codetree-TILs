n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
arr = []
arr_back=[]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            arr.append([i,j])
def back(m,new_arr,c):
    global arr, arr_back
    if len(new_arr) == m:
        arr_back.append(new_arr)
        return
    for i in range(c,len(arr)):
        back(m,new_arr+[arr[i]],i+1)

back(m,[],0)

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

def in_range(y,x):
    return x >=0 and x <= n-1 and y >= 0 and y <= n-1

def bfs(loc):
    global ans_visited
    d = [(0,-1),(1,0),(0,1),(-1,0)]
    ans = 0
    ans_visited = [[0]*n for _ in range(n)]
    for i in range(k):
        q.append((r[i],c[i]))
        visited = [[0]*n for _ in range(n)]
        visited[r[i]][c[i]] = 1
        while q:
            y,x = q.popleft()
            if ans_visited[y][x] == 0 and not [y,x] in arr_back[loc]:
                ans_visited[y][x] = 1
                ans +=1
            for j in range(len(d)):
                dy, dx = d[j]
                oy, ox = dy + y, dx+x
                if in_range(oy,ox) and (grid[oy][ox] != 1 or [oy,ox] in arr_back[loc]) and visited[oy][ox] ==0:
                    visited[oy][ox] = 1
                    q.append((oy,ox))
    return ans+m
            


from collections import deque
q = deque()
# oy,ox = 1,3
# print((grid[2][0] != 1 or [oy,ox] in [[1,2],[2,0]]))
ans = 0
for i in range(len(arr_back)):
    total = bfs(i)
    ans = max(ans,total)
print(ans)
# Please write your code here.

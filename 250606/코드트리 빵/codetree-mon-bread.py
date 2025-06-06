n,m = map(int,input().split())
arr = [list(map(int,input().split()))for _ in range(n)]
market = [list(map(int,input().split()))for _ in range(m)]
from collections import deque
visited = [[0]*n for _ in range(n)]
q = deque()
def in_range(y,x):
    return x >=0 and x <=n-1 and y >=0 and y <=n-1
def push(y,x,s):
    visited[y][x] = s

def bfs():
    global visited
    d = [(-1,0),(0,-1),(0,1),(1,0)]
    while q:
        y,x = q.popleft()
        for loc in range(len(d)):
            dy, dx = d[loc]
            oy, ox = dy +y, dx +x
            if in_range(oy,ox) and visited[oy][ox] ==0 and arr[oy][ox] !=2:
                push(oy,ox,visited[y][x]+1)
                q.append((oy,ox))

people = [(-1,-1)]*m # for _ in range(m)
curr = 0
# print(people)
# print(people[0] == (-1,-1))

cnt = 0 
while cnt != m:
    curr +=1
    for i in range(m):
        if people[i] == (-1,-1):
            continue
        qy,qx = market[i]
        qy -=1
        qx -=1
        visited = [[0]*n for _ in range(n)]
        visited[qy][qx] = 1
        q=deque()
        q.append((qy,qx))
        bfs()

        y,x = people[i]
        d = [(-1,0),(0,-1),(0,1),(1,0)]
        min_loc = 999999
        for loc in range(len(d)):
            dy, dx = d[loc]
            oy, ox = dy +y, dx +x
            if in_range(oy,ox) and visited[oy][ox] and min_loc > visited[oy][ox]:
                min_loc =  visited[oy][ox]
                people[i] = (oy,ox)
        if people[i] == (qy,qx):
            people[i] = (-1,-1)
            arr[qy][qx] = 2
            cnt +=1

    if curr <=m:
        house = market[curr-1]
        visited = [[0]*n for _ in range(n)]
        q=deque()
        q.append((house[0]-1,house[1]-1))
        visited[house[0]-1][house[1]-1] = 1
        bfs()
        min_loc = (999999,999999,999999)
        for i in range(n):
            for k in range(n):
                if arr[i][k] == 1:
                    temp_loc = (visited[i][k],i,k)
                    if min_loc > temp_loc:
                        min_loc = temp_loc
        people[curr-1] = (min_loc[1],min_loc[2])
        arr[min_loc[1]][min_loc[2]] = 2
        # print(visited)
print(curr)


    



# for i in market:
#     arr[i[0]-1][i[1]-1] = 2
# print(n,m,arr,market)
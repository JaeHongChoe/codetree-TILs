n,t,p,cp,dp = map(int,input().split())
ry, rx = map(int,input().split())
player_ori = [list(map(int,input().split())) for _ in range(p)]
player=sorted(player_ori)
order_player=[0]*p
ry-=1
rx-=1
arr=[[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
from collections import deque
for i in range(p):
    player[i][1]-=1
    player[i][2]-=1
    player[i].append(0)
    player[i].append(0)
    arr[player[i][1]][player[i][2]] = player[i][0]
    order_player[i] = player_ori[i][0]-1
arr[ry][rx] = -1

def in_range(y,x):
    return x >=0 and x<n and y>=0 and y<n
def push(y,x,s):
    visited[y][x]=s

def bfs(y,x):
    global visited
    d = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
    q = deque()
    q.append((y,x))
    visited = [[0]*n for _ in range(n)]
    player_check = [0]*p
    visited[y][x] = 1
    while q:
        y,x = q.popleft()
        for loc in range(len(d)):
            dy, dx = d[loc]
            oy, ox = dy+y, dx+x
            if in_range(oy,ox) and visited[oy][ox] ==0:
                push(oy,ox,visited[y][x]+1)
                q.append((oy,ox))
def bfssan(y,x):
    global visited
    d = [(-1,0),(0,1),(1,0),(0,-1)]
    q = deque()
    q.append((y,x))
    visited = [[0]*n for _ in range(n)]
    player_check = [0]*p
    visited[y][x] = 1
    while q:
        y,x = q.popleft()
        for loc in range(len(d)):
            dy, dx = d[loc]
            oy, ox = dy+y, dx+x
            if in_range(oy,ox) and visited[oy][ox] ==0:
                push(oy,ox,visited[y][x]+1)
                q.append((oy,ox))
def find_loc():
    min_loc = (99999,99999,99999)
    for i in range(p):
        ppp,y,x,_,_ = player[i]
        if ppp == -1:
            continue
        if min_loc > (visited[y][x],y*-1,x*-1):
            min_loc = (visited[y][x],y*-1,x*-1)
    return min_loc

def moveru():
    global arr,ry,rx,player,player_ori
    d = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
    dist = 99999
    dist_k = -1
    temp_arr = [[0]*n for _ in range(n)]
    for loc in range(len(d)):
        dy, dx = d[loc]
        oy, ox = dy+ry, dx+rx
        if in_range(oy,ox):
            temp = (oy-min_loc[1]*-1)**2 + (ox-min_loc[2]*-1)**2 
            if dist > temp:
                dist=temp
                dist_k = loc
    if dist==0:
        dy, dx = d[dist_k]
        oy, ox = dy+ry, dx+rx
        arr[ry][rx]=0
        temp_arr[oy][ox] = -1
        first_player = arr[oy][ox]
        arr[dy+ry][dx+rx] = 0
        player[first_player-1][4]+=cp
        player[first_player-1][3]+=2
        for _ in range(cp):
            oy, ox = oy+dy, ox+dx
        if in_range(oy,ox) and arr[oy][ox] ==0:
            temp_arr[oy][ox] = first_player
        elif in_range(oy,ox) and arr[oy][ox] !=0:
            temp_arr[oy][ox] = first_player
            ty,tx = oy,ox
            while True:
                ty,tx= ty+dy, tx+dx
                if not in_range(ty,tx):
                    player[arr[ty+(dy*-1)][tx+(dx*-1)]-1][0]=-1
                    # player[arr[ty+(dy*-1)][tx+(dx*-1)]-1][3]=2
                    arr[ty+(dy*-1)][tx+(dx*-1)] = 0
                    break
                temp_arr[ty][tx] = arr[ty+(dy*-1)][tx+(dx*-1)]
                arr[ty+(dy*-1)][tx+(dx*-1)] = 0
                if arr[ty][tx] ==0:
                    break
        elif not in_range(oy,ox):
            player[first_player-1][0]=-1
    else:
        dy, dx = d[dist_k]
        oy, ox = dy+ry, dx+rx
        arr[ry][rx] = 0
        temp_arr[oy][ox] = -1
    ry+= d[dist_k][0]
    rx+= d[dist_k][1]
    for i in range(n):
        for k in range(n):
            if arr[i][k] !=0 and temp_arr[i][k]==0:
                temp_arr[i][k] = arr[i][k]
            if temp_arr[i][k] !=0 and temp_arr[i][k] !=-1:
                player[temp_arr[i][k]-1][1]=i
                player[temp_arr[i][k]-1][2]=k
    arr= temp_arr


def movesan(sy,sx):
    global arr,ry,rx,player,player_ori
    # print(arr,"start")
    d = [(-1,0),(0,1),(1,0),(0,-1)]
    dist = 99999
    dist_k = -1
    temp_arr = [[0]*n for _ in range(n)]
    for loc in range(len(d)):
        dy, dx = d[loc]
        oy, ox = dy+sy, dx+sx
        if in_range(oy,ox):
            temp1 = visited[oy][ox] - visited[sy][sx] 
            temp = (oy-ry)**2 + (ox-rx)**2 
            if dist > temp and (arr[oy][ox] ==0 or arr[oy][ox] ==-1) and temp1 == -1:
                dist=temp
                dist_k=loc
    if dist_k==-1:
        return
    # print(dist, dist_k)
    # print("Arr")
    # print(arr)
    # print("temp_arr")
    # print(temp_arr)
    if dist==0:
        dy, dx = d[dist_k]
        oy, ox = dy+sy, dx+sx
        first_player = arr[sy][sx]
        arr[sy][sx]=0
        player[first_player-1][4]+=dp
        player[first_player-1][3]+=1
        dy*=-1
        dx*=-1
        for _ in range(dp):
            oy, ox = oy+dy, ox+dx
        if in_range(oy,ox) and arr[oy][ox] ==0:
            temp_arr[oy][ox] = first_player
        elif in_range(oy,ox) and arr[oy][ox] !=0:
            ty,tx = oy,ox
            temp_arr[oy][ox] = first_player
            while True:
                ty,tx= ty+dy, tx+dx
                if not in_range(ty,tx):
                    player[arr[ty+(dy*-1)][tx+(dx*-1)]-1][0]=-1
                    arr[ty+(dy*-1)][tx+(dx*-1)] = 0
                    break
                temp_arr[ty][tx] = arr[ty+(dy*-1)][tx+(dx*-1)]
                arr[ty+(dy*-1)][tx+(dx*-1)] = 0
                if arr[ty][tx] ==0:
                    break
        elif not in_range(oy,ox):
            player[first_player-1][0]=-1
    else:
        dy, dx = d[dist_k]
        oy, ox = dy+sy, dx+sx
        temp_arr[oy][ox] = arr[sy][sx]
        arr[sy][sx] = 0
    for i in range(n):
        for k in range(n):
            if arr[i][k] !=0 and temp_arr[i][k]==0:
                if player[arr[i][k]-1][0] == -1 and arr[i][k] !=-1:
                    continue
                temp_arr[i][k] = arr[i][k]
            if temp_arr[i][k] !=0 and temp_arr[i][k] !=-1:
                player[temp_arr[i][k]-1][1]=i
                player[temp_arr[i][k]-1][2]=k
    temp_arr[ry][rx]=-1
    arr= temp_arr
    # print(temp_arr)
    # print("루돌푸:",ry,rx)
    # print(player_ori)
    # print(dist,dist_k)
    # return temp_arr


q=deque()
for kkk in range(t):
    bfs(ry,rx)
    # print(visited)
    min_loc = find_loc()
    # print(min_loc)

    moveru()

    for i in range(p):
        orp = order_player[i]
        orp = i
        if player[orp][0] == -1:
            continue
        if player[orp][3] > 0:
            player[orp][3] -=1
            player[orp][4] +=1
            continue
        _,y,x,_,_ = player[orp]
        bfssan(ry,rx)
        movesan(y,x)
        if player[orp][0] != -1:
            player[orp][4] +=1
for i in range(p):
    print(player[i][4],end=" ")


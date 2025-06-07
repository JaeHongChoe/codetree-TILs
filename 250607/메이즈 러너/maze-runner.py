n, p, t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

# arr = [[0]*n for _ in range(n)]
player = [list(map(int,input().split())) for _ in range(p)]
exit = list(map(int,input().split()))
visited = [[0]*n for _ in range(n)]
for i in range(p):
    player[i]=player[i][0]-1,player[i][1]-1
exit = exit[0]-1,exit[1]-1


def push(y,x,s):
    visited[y][x]=s
def in_range(y,x):
    return x >=0 and x <=n-1 and y>=0 and y <=n-1

def bfs():
    d = [(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        y,x = q.popleft()
        for loc in range(len(d)):
            dy, dx = d[loc]
            oy, ox = dy+y, dx+x
            if in_range(oy,ox) and visited[oy][ox]==0:
                push(oy,ox,visited[y][x]+1)
                q.append((oy,ox))
        # if (oy,ox)==(exit):
        #     print(visited)
        #     return
def sim():
    global visited,q,move
    d = [(-1,0),(1,0),(0,-1),(0,1)]
    y,x = exit
    visited = [[0]*n for _ in range(n)]
    visited[y][x]=1
    q = deque()
    q.append((y,x))
    bfs()
    # print(visited)
    # print(arr)

    for i in range(p):
        if player[i] ==(-1,-1):
            continue
        y, x = player[i]
        ty, tx = player[i]
        q=deque()
        q.append((y,x))
        # for _ in range(visited[qy][qx]):
        cnt=0
        min_loc = (visited[y][x],3,99999,99999)
        qy,qx,=q.popleft()
        for loc in range(len(d)):
            dy, dx = d[loc]
            oy, ox = dy+qy, dx+qx
            if in_range(oy,ox) and arr[oy][ox] == 0:
                temp_loc = (visited[oy][ox],loc,oy,ox)
                if min_loc>temp_loc:
                    min_loc = temp_loc
                    ty,tx = min_loc[2],min_loc[3]
                    move+=1
                    y,x = ty,tx
                    q=deque()
                    break

            cnt+=1
        # print(y,x,exit)
        if (y,x) == exit:
            # print(y,x,"sdfjsnfjsf")
            y,x= -1,-1
        player[i] = y,x

        # print(player,curr,move)
    find_grid()

def sim1():
    global visited,q,move
    d = [(-1,0),(1,0),(0,-1),(0,1)]
    y,x = exit
    visited = [[0]*n for _ in range(n)]
    visited[y][x]=1
    q = deque()
    q.append((y,x))
    bfs()
    # print(visited)
    # print(arr)

    for i in range(p):
        if player[i] ==(-1,-1):
            continue
        y, x = player[i]
        ty, tx = player[i]
        q=deque()
        q.append((y,x))
        # for _ in range(visited[qy][qx]):
        cnt=0
        min_loc = (visited[y][x],3,99999,99999)
        while q:
            qy,qx,=q.popleft()
            for loc in range(len(d)):
                dy, dx = d[loc]
                oy, ox = dy+qy, dx+qx
                if in_range(oy,ox) and visited[oy][ox]:
                    temp_loc = (visited[oy][ox],loc,oy,ox)
                    if min_loc>temp_loc and arr[oy][ox] == 0:
                        min_loc = temp_loc
                        q.append((oy,ox))
                        if cnt ==0:
                            ty,tx = min_loc[2],min_loc[3]
                        if (oy,ox)==exit:
                            move+=1
                            y,x = ty,tx
                            q=deque()
                            break

            cnt+=1
        # print(y,x,exit)
        if (y,x) == exit:
            # print(y,x,"sdfjsnfjsf")
            y,x= -1,-1
        player[i] = y,x

        # print(player,curr,move)
    find_grid()

def find_grid():
    global arr
    temp_arr = arr
    for i in range(p):
        y,x = player[i]
        if (y,x) != (-1,-1):
            temp_arr[y][x] = -1
    temp_arr[exit[0]][exit[1]] = -2
    for i in range(1,n+1):
        for y in range(n-i):
            for x in range(n-i):
                if not (exit[0] >= y and exit[0] <= y+i and exit[1] >= x and exit[1] <=x+i):
                    continue
                for my in range(y,y+i+1):
                    for mx in range(x,x+i+1):
                        if temp_arr[my][mx] == -1:
                            temp_arr = rotate(y,x,i+1,temp_arr)
                            return
       
def rotate(sy,sx,length,temp_arr):
    global exit
    new_arr = [[0]*n for _ in range(n)]
    for i in range(sy,sy+length):
        for k in range(sx, sx+length):
            dy, dx = i - sy, k - sx
            oy, ox = dx, length - 1 - dy
            new_arr[sy+oy][sx+ox] = temp_arr[i][k]
            if temp_arr[i][k]==-2:
                exit = sy+oy,sx+ox
                temp_arr[i][k]=0
                new_arr[sy+oy][sx+ox]=0
            if temp_arr[i][k]==-1:
                for loc in range(p):
                    if player[loc] ==(i,k):
                        player[loc] = (sy+oy,sx+ox)

    # print(new_arr)
    for i in range(sy,sy+length):
        for k in range(sx, sx+length):
            if new_arr[i][k] == -1:
                temp_arr[i][k] = new_arr[i][k]+1
            elif new_arr[i][k] !=0:
                temp_arr[i][k] = new_arr[i][k]-1
            else:
                temp_arr[i][k] = new_arr[i][k]
    for i in range(n):
        for k in range(n):
            if temp_arr[i][k] == -1:
                temp_arr[i][k]=0
    return temp_arr


    

curr =0
move=0
from collections import deque
q = deque()
while curr != t:
    curr+=1
    sim()
    
print(move)
print(exit[0]+1,exit[1]+1)

import sys
sys.stdin = open("./input.txt")
input = sys.stdin.readline

from collections import deque
n, t, p, rp, sp = map(int,input().split())
ry,rx = map(int,input().split())
player_arr = [list(map(int,input().split())) for _ in range(p)]
arr = [[0]*n for _ in range(n)]
ry-=1
rx-=1
visited = [[0]*n for _ in range(n)]
for i in range(p):
    pp, y,x = player_arr[i]
    player_arr[i] = [pp,y-1,x-1,0,0]
    arr[y-1][x-1] = pp
arr[ry][rx] = -1

def in_range(y,x):
    return x>=0 and x<n and y>=0 and y<n

def push(y,x,s):
    visited[y][x]=s

def find_loc(d,ori_y,ori_x,type):
    global visited
    q=deque()
    visited = [[0]*n for _ in range(n)]
    visited[ori_y][ori_x]=1
    q.append((ori_y,ori_x))
    while q:
        y,x = q.popleft()
        for loc in range(len(d)):
            dy,dx = d[loc]
            oy,ox = y+dy, dx+x
            if in_range(oy,ox) and visited[oy][ox]==0:
                push(oy,ox,visited[y][x]+1)
                q.append((oy,ox))
    ## type=0 ru, type=1 san
    if type ==0:
        min_loc = (99999, 99999, 99999)
        for i in range(p):
            _, y, x, _, _ = player_arr[i]
            if (-1,-1) ==(y,x):
                continue
            # temp = (visited[y][x], y * -1, x * -1)
            temp = (((y - ry) ** 2) + ((x - rx) ** 2), y * -1, x * -1)
            if min_loc>temp:
                min_loc=temp
        return find_move_loc(d,visited, min_loc)


def find_loc_san(d,ori_y,ori_x,san_y,san_x):
    global visited
    q=deque()
    visited = [[0]*n for _ in range(n)]
    visited[ori_y][ori_x]=1
    q.append((ori_y,ori_x))
    min_loc = (99999, 99999)
    to_return=(-1,-1)
    while q:
        y,x = q.popleft()
        for loc in range(len(d)):
            dy,dx = d[loc]
            oy,ox = y+dy, dx+x
            if in_range(oy,ox) and visited[oy][ox]==0 and (arr[oy][ox]==0 or arr[oy][ox]==-1):
                push(oy,ox,visited[y][x]+1)
                q.append((oy,ox))
    for loc in range(len(d)):
        dy, dx = d[loc]
        oy, ox = san_y + dy, dx + san_x
        if in_range(oy,ox) and visited[oy][ox]!=0:
            temp = (((oy - ry) ** 2) + ((ox - rx) ** 2),loc)
            # temp = (visited[oy][ox], loc)
            if min_loc > temp:
                min_loc = temp
                to_return = (oy, ox)
    # temp_y,temp_x=to_return
    if ((san_y - ry) ** 2) + ((san_x - rx) ** 2) < min_loc[0]:
        to_return=(-1,-1)
    return to_return,min_loc[1]


def find_move_loc(d,visited,min_loc):
    global arr
    y,x = ry,rx
    min_score = 99999
    min_dir = [99999,-1,-1,-1]
    _,san_y,san_x = min_loc
    san_x*=-1
    san_y*=-1
    for loc in range(len(d)):
        dy, dx = d[loc]
        oy, ox = y + dy, dx + x
        if in_range(oy,ox):
            temp = ((oy-san_y)**2)+((ox-san_x)**2)
            if min_score>temp:
                min_score=temp
                min_dir=[temp,oy,ox,loc]
    return min_dir

def relations(to_y,to_x,loc,power):
    y,x = to_y,to_x
    dy,dx=loc
    temp=[]
    while True:
        tt=arr[y][x]
        y,x = y+dy,x+dx
        if in_range(y,x) and arr[y][x] !=0:
            temp.append([y,x,tt])
        elif in_range(y,x) and arr[y][x] ==0:
            temp.append([y, x,tt])
            break
        elif not in_range(y,x):
            dy*=-1
            dx*=-1
            y,x = dy+y, dx+x
            pp=arr[y][x]
            for i in range(p):
                if player_arr[i][0] == pp:
                    player_arr[i][1],player_arr[i][2] = -1,-1
                    break
            break
    for i in range(len(temp)):
        y,x,pp=temp[i]
        for i in range(p):
            if player_arr[i][0] == pp:
                arr[y][x]=pp
                player_arr[i][1], player_arr[i][2] = y, x


def move_ru():
    global ry,rx,cp
    d = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    min_dir = find_loc(d,ry,rx,0)
    dist,y,x,loc = min_dir
    if dist ==0:
        dy,dx=d[loc]
        to_x = x+(dx*rp)
        to_y = y+(dy*rp)
        #점수 올리기
        for idx_p in range(p):
            if (player_arr[idx_p][1],player_arr[idx_p][2]) == (y,x):
                player_arr[idx_p][4] += rp
                player_arr[idx_p][3] =2
                ppp = player_arr[idx_p][0]

        if in_range(to_y,to_x) and (arr[to_y][to_x] ==0 or arr[to_y][to_x] !=0):
            relations(to_y,to_x,(dy,dx),rp)
            for i in range(p):
                if player_arr[i][0] == ppp:
                    arr[y][x]=0
                    arr[to_y][to_x] = ppp
                    player_arr[i][1], player_arr[i][2] = to_y, to_x
        #die
        elif not in_range(to_y,to_x):
            for i in range(p):
                if player_arr[i][0] == ppp:
                    arr[y][x]=0
                    # arr[to_y][to_x] = ppp
                    player_arr[i][1], player_arr[i][2] = -1, -1

    arr[y][x] = -1
    arr[ry][rx] = 0
    ry, rx = y, x

def move_san():
    d = [(-1,0),(0,1),(1,0),(0,-1)]
    for i in range(p):
        ppp,y,x,stop,score = player_arr[i]
        if (y,x)==(-1,-1):
            continue
        if stop >0:
            player_arr[i][3]-=1
            continue
        min_dir,loc = find_loc_san(d, ry, rx,y,x)
        sy,sx=min_dir
        if (sy,sx) == (ry,rx):
            dy, dx = d[loc]
            dy*=-1
            dx*=-1
            to_x = sx + (dx * sp)
            to_y = sy + (dy * sp)
            # 점수 올리기
            for idx_p in range(p):
                if (player_arr[idx_p][1], player_arr[idx_p][2]) == (y, x):
                    player_arr[idx_p][4] += sp
                    player_arr[idx_p][3] = 1
                    ppp = player_arr[idx_p][0]
            if in_range(to_y, to_x) and (arr[to_y][to_x] == 0 or arr[to_y][to_x] != 0):
                relations(to_y, to_x, (dy, dx), sp)
                for i in range(p):
                    if player_arr[i][0] == ppp:
                        arr[y][x] = 0
                        arr[to_y][to_x] = ppp
                        player_arr[i][1], player_arr[i][2] = to_y, to_x
            # die
            elif not in_range(to_y, to_x):
                for i in range(p):
                    if player_arr[i][0] == ppp:
                        arr[y][x] = 0
                        # arr[to_y][to_x] = ppp
                        player_arr[i][1], player_arr[i][2] = -1, -1
        elif (sy,sx) !=(-1,-1):
            for i in range(p):
                if player_arr[i][0] == ppp:
                    arr[y][x] = 0
                    arr[sy][sx] = ppp
                    player_arr[i][1], player_arr[i][2] = sy, sx
    for i in range(p):
        ppp,y,x,stop,score = player_arr[i]
        if (y,x)==(-1,-1):
            continue
        player_arr[i][4]+=1

for times in range(t):
    move_ru()

    move_san()
    new=[[0]*n for _ in range(n)]
    for i in range(p):
        ppp,y,x,_,_ = player_arr[i]
        new[y][x] =ppp
    new[ry][rx]=-1
    arr=new
player_arr=sorted(player_arr)
for i in range(p):

    print(player_arr[i][4],end=" ")

import sys
sys.stdin = open("./input.txt")
input = sys.stdin.readline

from collections import deque
n,p=map(int,input().split())
my,mx,py,px = map(int,input().split())
t_arr= list(map(int,input().split()))
block_arr = [list(map(int,input().split())) for _ in range(n)]
move_arr = [[0]*n for _ in range(n)]
sight_arr = [[0]*n for _ in range(n)]
man_arr=[[0]  for _ in range(p)]
cnt=0
for i in range(0,p*2,2):
    y,x = t_arr[i:i + 2]
    man_arr[cnt] = [y,x]
    move_arr[y][x] = 1
    cnt+=1
move_arr[my][mx]=2

def in_range(y,x):
    return x>=0 and x<n and y>=0 and y<n

def find_home():
    q= deque()
    q.append((my,mx))
    dist_arr = [[0]*n for _ in range(n)]
    dist_arr[my][mx]=(my,mx)
    visited = [[0]*n for _ in range(n)]
    visited[my][mx] =1
    d = [(-1,0),(1,0),(0,-1),(0,1)] #상하좌우
    medu=[]
    while q:
        y,x = q.popleft()
        if (y,x)==(py,px):
            medu.append((y, x))
            while True:
                y,x = dist_arr[y][x]
                if (y, x) == (my, mx):  return medu[::-1]
                medu.append((y,x))
        dist = (99999,9)
        for loc in range(len(d)):
            dy,dx = d[loc]
            oy,ox = dy+y,dx+x
            if in_range(oy,ox) and visited[oy][ox] ==0 and block_arr[oy][ox]==0:
                visited[oy][ox]=1
                temp = (abs(oy-py) + abs(ox-px),loc*-1)
                if dist > temp:
                    dist=temp
                    q.append((oy,ox))
                    dist_arr[oy][ox] = (y,x)
    print(visited)
    return -1

def count_map_sight():
    d=[(-1,0),(1,0),(0,-1),(0,1)]
    best_arr=[]
    got_man=(0,9)
    for loc in range(len(d)):
        tt_arr = [[0] * n for _ in range(n)]
        cnt=0
        y,x = d[loc]
        good=True
        sy, sx = my, mx
        while True:
            sy+=y
            sx+=x
            if not in_range(sy,sx):
                break
            if good:    tt_arr[sy][sx]=1
            else:   tt_arr[sy][sx]=2
            if [sy,sx] in man_arr:
                cnt+=man_arr.count([sy,sx])
                good=False

        for k in range(2):
            if k ==0:   dy,dx= y+x*-1,x+y*-1
            else:   dy,dx= y+x,x+y
            ny,nx = my, mx
            good=True
            while True:
                ny,nx = ny+dy,nx+dx
                if not in_range(ny, nx):    break
                if good:
                    tt_arr[ny][nx] = 1
                    if [ny, nx] in man_arr:
                        cnt += man_arr.count([ny, nx])
                        good = False
                else:   tt_arr[ny][nx] = 2
                t_good=True
                side_y, side_x = ny,nx
                while True:
                    side_y += y
                    side_x += x
                    if not in_range(side_y, side_x):    break
                    if t_good and good:
                        tt_arr[side_y][side_x] = 1
                        if [side_y, side_x] in man_arr:
                            cnt += man_arr.count([side_y, side_x])
                            t_good = False
                    else:   tt_arr[side_y][side_x] = 2

        temp = (cnt, loc*-1)
        if got_man <temp:
            got_man=temp
            best_arr=tt_arr
    return best_arr,got_man

def bfs_man(y,x,best_map):
    d = [[(-1, 0), (1, 0), (0, -1), (0, 1)],[(0,-1),(0,1),(-1,0),(1,0)]]
    move_loc = (y,x,0)
    for i in range(len(d)):
        dist = abs(my - y) + abs(mx - x)
        for loc in range(len(d[0])):
            dy,dx = d[i][loc]
            oy,ox = dy+y,dx+x
            if in_range(oy,ox) and best_map[oy][ox]!=1:
                tdist = abs(my - oy) + abs(mx - ox)
                if dist > tdist:
                    dist=tdist
                    move_loc=(oy,ox,i+1)
        y,x,_=move_loc
        if dist==0:
            return 1,move_loc
    return 0,move_loc




### 메두사이동
tt = find_home()
if tt == -1:
    print(-1)
else:
    for sy,sx in tt:
        if (sy,sx) == (py,px):
            print(0)
            break
        move_arr[my][mx]=0
        move_arr[sy][sx]=2
        my=sy
        mx=sx
        if [sy,sx] in man_arr:
            man_arr.remove([sy,sx])

        ##메두사 시선 카운트, 카운트 찾고 시야 정보 리턴
        best_map, stone_count = count_map_sight()
        # print(best_map,stone_count)
        if len(best_map)==0:
            print(0,0,0)
            continue

        ## 전사  이동, 멘하탄 거리 기준, 시야정보에서 1이면 못 움직이임
        attck_score=0
        move_score = 0
        for i in range(len(man_arr)):
            y,x = man_arr.pop(0)
            # print(y,x)
            if best_map[y][x] ==1:
                man_arr.append([y, x])
                continue
            score, to_move = bfs_man(y,x,best_map)
            move_score += to_move[2]
            if score ==1:
                attck_score+=1
            else:
                move_arr[y][x]=0
                move_arr[to_move[0]][to_move[1]]=1
                man_arr.append((to_move[0],to_move[1]))

        print(move_score,stone_count[0],attck_score)
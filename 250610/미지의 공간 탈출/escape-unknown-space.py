import sys
sys.stdin = open("./input.txt")
input = sys.stdin.readline
from collections import deque
n,m,f = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

east_arr = [list(map(int,input().split())) for _ in range(m)]
west_arr = [list(map(int,input().split())) for _ in range(m)]
south_arr = [list(map(int,input().split())) for _ in range(m)]
north_arr = [list(map(int,input().split())) for _ in range(m)]
top_arr = [list(map(int,input().split())) for _ in range(m)]

f_arr =  [list(map(int,input().split())) for _ in range(f)]
q = deque()
visited = [[0]*n for _ in range(n)]
def in_range(y,x):
    return x >=0 and x <n and y >=0 and y <n

def find_exit_map():
    d = [(0,-1),(1,0),(0,1),(-1,0)]
    check=(-1,-1)
    for i in range(n):
        for k in range(n):
            if arr[i][k] !=0:
                continue
            f_check=-1
            b_check=-1
            for loc in range(len(d)):
                dy, dx = d[loc]
                oy, ox = dy+i, dx+k
                if in_range(oy,ox):
                    if arr[oy][ox] ==3:
                        f_check+=1
                    if arr[oy][ox]==1:
                        b_check+=1
            if (f_check, b_check) == (0,1):
                for loc in range(len(d)):
                    dy, dx = d[loc]
                    oy, ox = dy + i, dx + k
                    if arr[oy][ox] == 0:
                        return (i,k),loc
    return -1, -1
def push(y,x,s):
    visited[y][x]=s
def bfs(idx,arr,nn,fisrt=True):
    global visited
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    y,x = idx
    q = deque()
    q.append((y,x))
    visited = [[0] * nn for _ in range(nn)]
    if fisrt:
        visited[y][x]=1
    else:
        visited[y][x] = side_exit_value
    while q:
        y,x = q.popleft()
        for loc in range(len(d)):
            dy, dx = d[loc]
            oy, ox = dy + y, dx + x
            if in_range(oy, ox) and visited[oy][ox] ==0 and arr[oy][ox]==0:
                push(oy,ox,visited[y][x]+1)
                q.append((oy,ox))
    return visited

def bfs_three(idx,arr,nn):
    global visited
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    y,x = idx
    q = deque()
    q.append((y,x))
    visited = [[0]*nn for _ in range(nn)]
    visited[y][x]=1
    while q:
        y,x = q.popleft()
        for loc in range(len(d)):
            dy, dx = d[loc]
            oy, ox = dy + y, dx + x
            if in_range(oy, ox) and visited[oy][ox] ==0 and (arr[oy][ox]==0):
                if arr[oy][ox]==0:
                    push(oy,ox,visited[y][x]+1)
                    q.append((oy,ox))
                # elif arr[oy][ox]==-1:
                #     push(oy, ox, visited[y][x])
                #     q.append((oy, ox))
                    # visited[oy][ox]=visited[y][x]
    return visited

def bfs_side():
    global visited,threed_side_visit, threed_side_map
    d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    num_y = len(threed_side_visit)
    num_x = len(threed_side_visit[0])
    # visited = [[0]*num_y for _ in range(num_x)]
    for i in range(num_y):
        for k in range(num_x):
            if threed_side_visit[i][k]!=0 and threed_side_map[i][k] !=1:
                q = deque()
                q.append((i,k))
                while q:
                    y,x = q.popleft()
                    for loc in range(len(d)):
                        dy, dx = d[loc]
                        oy, ox = dy + y, dx + x
                        if oy >=0 and oy < num_y and ox >=0 and ox < num_x and threed_side_visit[oy][ox]==0 and threed_side_map[oy][ox] !=1:
                            threed_side_visit[oy][ox]=threed_side_visit[y][x]+1
                            q.append((oy,ox))
                        elif oy >=0 and oy < num_y and (ox <0 or ox >= num_x):
                            if ox <0:
                                ox=m-1
                            elif ox >=num_x:
                                ox=1
                            if threed_side_visit[oy][ox]==0 and threed_side_map[oy][ox] !=1:
                                threed_side_visit[oy][ox]=threed_side_visit[y][x]+1
                                q.append((oy,ox))

                            # elif arr[oy][ox]==-1:
                            #     push(oy, ox, visited[y][x])
                            #     q.append((oy, ox))
                                # visited[oy][ox]=visited[y][x]
    return visited

def make_threed_map():
    global threed_map
    temp_map = [[1]*n for _ in range(n)]
    mx=0
    my=0
    move_count=0
    for i in range(1,10):
        if i in [1,3,7,9]:
            cover_map = temp_map
        elif i == 2:
            #180
            cover_map = [row[::-1]for row in north_arr[::-1]]
        elif i == 4:
            #90
            cover_map = list(map(list,zip(*west_arr[::-1])))
        elif i ==5:
            #top
            cover_map = top_arr
        elif i ==6:
            #270
            cover_map = list(map(list,zip(*east_arr)))[::-1]
        elif i ==8:
            cover_map= south_arr
        for y in range(my,m+my):
            for x in range(mx,m+mx):
                threed_map[y][x] = cover_map[y-my][x-mx]
        mx+=m
        move_count+=1
        if move_count==3:
            move_count=0
            mx=0
            my+=m
    for i in range(3*m):
        for k in range(3*m):
            if threed_map[i][k]==2:
                return (i,k)

def find_exit_threed(exit_idx):
    global threed_visited_map
    mx=0
    my=0
    move_count=0
    for i in range(1,10):
        temp_map = [[0] * m for _ in range(m)]
        if i in [1, 3, 7, 9,5]:
            mx += m
            move_count += 1
            if move_count == 3:
                move_count = 0
                mx = 0
                my += m
            continue

        for y in range(my,m+my):
            for x in range(mx,m+mx):
                temp_map[y - my][x - mx] = threed_visited_map[y][x]
        mx+=m
        move_count+=1
        if move_count==3:
            move_count=0
            mx=0
            my+=m
        if i == 2:
            #180 -> 180
            north_cover_map = [row[::-1]for row in temp_map[::-1]]
        elif i == 4:
            #90 -> 270
            west_cover_map = list(map(list, zip(*temp_map)))[::-1]
        elif i ==6:
            #270 ->90
            east_cover_map = list(map(list, zip(*temp_map[::-1])))
        elif i ==8:
            south_cover_map= temp_map

    tt = [[] for _ in range(m)]
    t2 = [[] for _ in range(m)]
    for tmtm in range(m):
        tt[tmtm].extend(south_cover_map[tmtm])
        tt[tmtm].extend(east_cover_map[tmtm])
        tt[tmtm].extend(north_cover_map[tmtm])
        tt[tmtm].extend(west_cover_map[tmtm])

        t2[tmtm].extend(south_arr[tmtm])
        t2[tmtm].extend(east_arr[tmtm])
        t2[tmtm].extend(north_arr[tmtm])
        t2[tmtm].extend(west_arr[tmtm])

    # if exit_idx ==0:
    #     for tmtm in range(m):
    #         tt[tmtm].extend(north_cover_map[tmtm])
    #         tt[tmtm].extend(west_cover_map[tmtm])
    #         tt[tmtm].extend(south_cover_map[tmtm])
    #         tt[tmtm].extend(east_cover_map[tmtm])
    #         tt[tmtm].extend(north_cover_map[tmtm])
    #
    #         t2[tmtm].extend(north_arr[tmtm])
    #         t2[tmtm].extend(west_arr[tmtm])
    #         t2[tmtm].extend(south_arr[tmtm])
    #         t2[tmtm].extend(east_arr[tmtm])
    #         t2[tmtm].extend(north_arr[tmtm])
    # elif exit_idx ==1:
    #     for tmtm in range(m):
    #         tt[tmtm].extend(west_cover_map[tmtm])
    #         tt[tmtm].extend(south_cover_map[tmtm])
    #         tt[tmtm].extend(east_cover_map[tmtm])
    #         tt[tmtm].extend(north_cover_map[tmtm])
    #         tt[tmtm].extend(west_cover_map[tmtm])
    #
    #         t2[tmtm].extend(west_arr[tmtm])
    #         t2[tmtm].extend(south_arr[tmtm])
    #         t2[tmtm].extend(east_arr[tmtm])
    #         t2[tmtm].extend(north_arr[tmtm])
    #         t2[tmtm].extend(west_arr[tmtm])
    # elif exit_idx ==2:
    #     for tmtm in range(m):
    #         tt[tmtm].extend(south_cover_map[tmtm])
    #         tt[tmtm].extend(east_cover_map[tmtm])
    #         tt[tmtm].extend(north_cover_map[tmtm])
    #         tt[tmtm].extend(west_cover_map[tmtm])
    #         tt[tmtm].extend(south_cover_map[tmtm])
    #
    #         t2[tmtm].extend(south_arr[tmtm])
    #         t2[tmtm].extend(east_arr[tmtm])
    #         t2[tmtm].extend(north_arr[tmtm])
    #         t2[tmtm].extend(west_arr[tmtm])
    #         t2[tmtm].extend(south_arr[tmtm])
    # elif exit_idx ==3:
    #     for tmtm in range(m):
    #         tt[tmtm].extend(east_cover_map[tmtm])
    #         tt[tmtm].extend(north_cover_map[tmtm])
    #         tt[tmtm].extend(west_cover_map[tmtm])
    #         tt[tmtm].extend(south_cover_map[tmtm])
    #         tt[tmtm].extend(east_cover_map[tmtm])
    #
    #         t2[tmtm].extend(east_arr[tmtm])
    #         t2[tmtm].extend(north_arr[tmtm])
    #         t2[tmtm].extend(west_arr[tmtm])
    #         t2[tmtm].extend(south_arr[tmtm])
    #         t2[tmtm].extend(east_arr[tmtm])
    return tt,t2

def time_sleep():
    global arr
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(f):
        y,x,move_dir, many = f_arr[i]
        cnt=0
        while True:
            cnt+=1
            dy,dx = d[move_dir]
            oy, ox = dy+y, dx+x
            if in_range(oy,ox) and before_move[oy][ox] >= many*cnt:
                arr[oy][ox] = 1
                return False
            if not in_range(oy,ox) or arr[oy][ox] == 1 or arr[oy][ox] == 4:
                break
    return True
ex_num=(0,0)
for i in range(n):
    for k in range(n):
        if arr[i][k] == 4:
            ex_num=(i,k)
            break

exit_idx,exit_threed = find_exit_map()
flag1=True
if (exit_idx,exit_threed) == (-1,-1):
    print(-1)
    flag1=False

for i in range(f):
    y,x,_,_ = f_arr[i]
    arr[y][x]=1
if flag1:
    while True:
        first_map = bfs(exit_idx,arr,n)
        threed_map = [[0]*m*3 for _ in range(m*3)]
        idx = make_threed_map()
        threed_visited_map = bfs_three(idx,threed_map,m*3)
        threed_side_visit, threed_side_map = find_exit_threed(exit_threed)
        # print(threed_side_visit)
        # print(threed_side_map)
        # for i in range(len(threed_visited_map)):
        #     print(threed_visited_map[i])
        # print()
        bfs_side()
        # for i in range(len(threed_side_visit)):
        #     print(threed_side_visit[i])
        final_all = []
        final_side_visit=[[0]*m for _ in range(m)]

        # for y in range(my,m+my):
        #     for x in range(mx,m+mx):
        #         temp_map[y - my][x - mx] = threed_visited_map[y][x]

        for whe in range(0,(m*3)+1,m):
            final_side_visit = [[0] * m for _ in range(m)]
            for i in range(m):
                for k in range(whe,m+whe):
                    final_side_visit[i][k-whe] = threed_side_visit[i][k]
            final_all.append(final_side_visit)
        # print(final_all)

        if exit_threed==0:
            final_side_visit = list(map(list, zip(*final_all[3][::-1])))
        elif exit_threed == 1:
            final_side_visit = final_all[0]
            # 180
            # final_side_visit = [row[::-1] for row in final_side_visit[::-1]]
        elif exit_threed == 2:
            # 270
            final_side_visit = list(map(list, zip(*final_all[1])))[::-1]

            # final_side_visit = list(map(list, zip(*final_side_visit[::-1])))
        elif exit_threed == 3:
            # 180
            final_side_visit = [row[::-1] for row in final_all[2][::-1]]
            # final_side_visit = list(map(list, zip(*final_side_visit)))[::-1]
        # print(final_side_visit)
        t_y=-1
        t_x=-1
        for i in range(n):
            for k in range(n):
                if arr[i][k]==3 and (t_x,t_y)==(-1,-1):
                    t_x = k
                    t_y = i
                    break
        for i in range(m):
            for k in range(m):
                first_map[i+t_y][k+t_x] = final_side_visit[i][k]

        d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        dy, dx = d[exit_threed]

        side_exit_value = first_map[exit_idx[0]+dy*-1][exit_idx[1]+dx*-1]
        first_map[exit_idx[0]][exit_idx[1]] = side_exit_value
        before_move = bfs(exit_idx,arr,n,False)

        flag = time_sleep()
        min_num=99999
        if flag:
            y,x = ex_num
            for loc in range(len(d)):
                dy, dx = d[loc]
                oy, ox = dy+y, dx+x
                if in_range(oy,ox) and before_move[oy][ox] !=0:
                    temp_min = before_move[oy][ox]
                    if min_num>temp_min:
                        min_num=temp_min
            if min_num == 99999:
                print(-1)
            else:
                print(min_num+1)
            break



# print(side_exit_value)
#
#
# print(threed_side_visit)
#
# for i in range(n):
#     print(before_move[i])
# print()
# for i in range(n):
#     print(before_move[i])
# print()
# for i in range(m*3):
#     print(threed_map[i])
# print()
# for i in range(m*3):
#     print(threed_visited_map[i])
# print()
# for i in range(m*3):
#     print(threed_visited_map[i])
# print(first_map)

# [0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 4, 0, 0, 0, 0]
# [0, 0, 0, 2, 3, 4, 0, 0, 0]
# [0, 0, 0, 1, 2, 3, 0, 0, 0]
# [0, 0, 0, 2, 0, 4, 0, 0, 0]
# [0, 0, 0, 3, 4, 5, 0, 0, 0]
# [0, 0, 0, 4, 5, 0, 0, 0, 0]
# [0, 0, 0, 0, 6, 7, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0]
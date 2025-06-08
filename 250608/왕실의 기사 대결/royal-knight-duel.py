n, p, t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
player = [list(map(int,input().split())) for _ in range(p)]
times = [list(map(int,input().split())) for _ in range(t)]
arr_player = [[0]*n for _ in range(n)]
temp_dam = [0]*p
from collections import deque
for i in range(p):
    y,x,h,w,k=player[i]
    y-=1
    x-=1
    arr_player[y][x] = i+1
    temp_dam[i] = k
    for he in range(h):
        arr_player[y+he][x] = i+1
        for we in range(1,w):
            arr_player[y+he][x+we]= i+1

def in_range(y,x):
    return x >=0 and x <=n-1 and y >=0 and y <=n-1


def abletomove(order_p, order_m):
    d = [(-1,0),(0,1),(1,0),(0,-1)]
    y,x,h,w,k = player[order_p]
    y-=1
    x-=1
    # h-=1
    # w-=1
    q=deque()
    # q.append((y,x))
    for he in range(h):
        q.append((y+he,x))
        for we in range(1,w):
            q.append((y+he,x+we))
    check = False
    visited = [0]*p
    visited[order_p]=1
    while q:
        y,x = q.popleft()
        oy, ox = d[order_m]
        dy, dx = y+oy, x+ox
        if in_range(dy,dx) and arr[dy][dx]!=2:
            check = True
        if in_range(dy,dx) and arr_player[dy][dx]!=0 and arr[dy][dx]!=2:
            # print(arr_player[dy][dx], visited)
            if visited[arr_player[dy][dx]-1]==0:
                visited[arr_player[dy][dx]-1] = 1
                py,px,ph,pw,pk = player[arr_player[dy][dx]-1]
                py-=1
                px-=1
                # ph-=1
                # pw-=1
                # q.append((dy,dx))
                for we in range(ph):
                    q.append((py+we,px))
                    for he in range(1,pw):
                        q.append((py+we,px+he))
                # print(q,"Fdsfsfa")
        if not in_range(dy,dx) or arr[dy][dx]==2:
            check = False
            q=deque()
            break
    return check, visited
        

def moveandcount(order_p, order_m,move_check):
    d = [(-1,0),(0,1),(1,0),(0,-1)]
    temp_player = [[0]*n for _ in range(n)]
    oy,ox = d[order_m]
    for i in range(n):
        for k in range(n):
            if arr_player[i][k] and move_check[arr_player[i][k]-1] ==1:
                temp_player[i+oy][k+ox] = arr_player[i][k]
                if arr[i+oy][k+ox] == 1 and arr_player[i][k]-1 !=order_p:
                    player[arr_player[i][k]-1][4] -=1
            elif arr_player[i][k]:
                temp_player[i][k] = arr_player[i][k]
    for i in range(len(player)):
        y,x,h,w,k = player[i]
        if move_check[i] == 1:
            player[i][0] += oy
            player[i][1] += ox
            if k <= 0:
                for ii in range(n):
                    for kk in range(n):
                        if temp_player[ii][kk] == i+1:
                            temp_player[ii][kk] =0
    return temp_player

dam = 0
for order in times:
    order_p, order_m = order
    order_p-=1
    if player[order_p][4] <= 0:
        continue

    check,move_check = abletomove(order_p, order_m)

    if check:
        arr_player = moveandcount(order_p, order_m,move_check)
    # print(arr_player,check,order)
    
for i in range(p):
    if player[i][4] > 0:
        dam += temp_dam[i] - player[i][4]
print(dam)

import sys
sys.stdin = open("./input.txt")
input = sys.stdin.readline

n,p,tree,t = map(int,input().split())
player_arr = [list(map(int,input().split())) for _ in range(p)]
tree_arr = [list(map(int,input().split())) for _ in range(tree)]
arr = [[0]*n for _ in range(n)]

def tor_to_exit():
    # temp_arr = [[0] * n for _ in range(n)]
    y = len(arr)//2
    x = len(arr[0])//2
    d = [(-1,0),(0,1),(1,0),(0,-1)]
    dist =1
    move_count = 0
    d_idx=0
    v=[]
    v.append([y,x,0])
    num=1
    while True:
        for i in range(dist):
            num+=1
            dy, dx = d[d_idx]
            y+=dy
            x+=dx
            if (-1,0) == (y,x):
                y,x,d_idx = v[-1]
                d_idx =(d_idx + 2) % 4
                v[-1]=[y,x,d_idx]
                return [v,v[::-1]] #temp_arr
            # temp_arr[y][x]=num
            v.append([y,x,d_idx])
        move_count+=1
        d_idx = (d_idx+1)%4
        v[-1]=[y,x,d_idx]
        if move_count == 2:
            move_count=0
            dist+=1


def in_range(y,x):
    return x>=0 and x<n and y>=0 and y<n
def move_player():
    global arr
    temp_arr = [[0] * n for _ in range(n)]
    d = [(0,1),(1,0),(0,-1),(-1,0)]
    for i in range(p):
        y,x,s=player_arr[i]
        if (y,x,s)==(-1,-1,-1):
            continue
        if abs(ry-y)+abs(rx-x) <=3:
            dy,dx = d[s]
            if not in_range(dy+y,dx+x):
                s=(s+2)%4
                dy, dx = d[s]
                if in_range(dy + y, dx + x) and (dy + y, dx + x) != (ry, rx):
                    player_arr[i] = [dy + y, dx + x, s]
                    continue
            if in_range(dy+y,dx+x) and (dy+y,dx+x) != (ry,rx):
                player_arr[i]=[dy+y,dx+x,s]
                continue
            if in_range(dy+y,dx+x) and (dy+y,dx+x) == (ry,rx):
                s=(s+2)%4
                dy, dx = d[s]
                if in_range(dy + y, dx + x) and (dy + y, dx + x) != (ry, rx):
                    player_arr[i] = [dy + y, dx + x, s]
                    continue
    for i in range(p):
        y, x, s = player_arr[i]
        if (y,x,s)==(-1,-1,-1):
            continue
        temp_arr[y][x]=1
    return temp_arr

exit = tor_to_exit()
exit[0].pop(0)
exit[1].pop(0)
idx=0
exit_loc = 0
ry = len(arr)//2
rx = len(arr[0])//2

for i in range(p):
    y,x,s=player_arr[i]
    player_arr[i] = [y-1,x-1,s-1]
    arr[y-1][x-1]=1
arr[ry][rx]=2

ans=0
for i in range(t):
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    temp_cnt = 0
    temp_arr = [[0] * n for _ in range(n)]
    new_arr = move_player()
    arr=new_arr
    #attack
    ty,tx,td=exit[exit_loc][idx]
    ry=ty
    rx=tx
    if arr[ry][rx]==1:
        for ii in range(p):
            y, x, _ = player_arr[ii]
            if (y, x) == (ry, rx):
                player_arr[ii] = [-1, -1, -1]
                temp_cnt += 1
    arr[ry][rx]=2

    for k in range(tree):
        y,x=tree_arr[k]
        if arr[y-1][x-1]!=2:
            arr[y-1][x-1]=0

    dy,dx=d[td]
    oy,ox=ry,rx
    for k in range(3):
        if k!=0:
            oy,ox = oy+dy, ox+dx
        if in_range(oy,ox) and arr[oy][ox] ==1:
            for ii in range(p):
                y,x,_=player_arr[ii]
                if (y,x)==(oy,ox):
                    player_arr[ii]=[-1,-1,-1]
                    temp_cnt+=1
    ans+=(i+1)*temp_cnt
    idx = (idx + 1) % len(exit[exit_loc])
    if idx == len(exit[exit_loc])-1 and exit_loc==0:
        exit_loc = 1
    elif idx == len(exit[exit_loc]) - 1 and exit_loc == 1:
        exit_loc = 0
print(ans)
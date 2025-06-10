import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

from collections import deque
n,t = map(int,input().split())
temp_arr=[list(map(list,input().split())) for _ in range(n)]
player_arr=[list(map(int,input().split())) for _ in range(n)]

type_arr = [[0]*n for _ in range(n)]
for i in range(len(temp_arr)):
    for k in range (len(temp_arr)):
        type_arr[i][k] = temp_arr[i][0][k]


def morning():
    for i in range(n):
        for k in range(n):
            player_arr[i][k]+=1

def in_range(y,x):
    return x >=0 and x<n and y>=0 and y<n

def lunch():
    d=[(0,-1),(1,0),(0,1),(-1,0)]
    visited = [[0]*n for _ in range(n)]
    group=[]
    for i in range(n):
        for k in range(n):
            if visited[i][k]==0:
                visited[i][k]=1
                type=type_arr[i][k]
                v=[]
                v.append([i,k])
                q = deque()
                q.append((i,k))
                while q:
                    y,x = q.popleft()
                    for loc in range(len(d)):
                        dy,dx = d[loc]
                        oy,ox = y+dy, x+dx
                        if in_range(oy,ox) and visited[oy][ox] ==0 and type_arr[oy][ox]==type:
                            v.append([oy,ox])
                            q.append((oy,ox))
                            visited[oy][ox]=1
                max_loc = (-1,99999,99999)
                for test_i in range(len(v)):
                    y,x = v[test_i]
                    player_arr[y][x]-=1
                    temp = (player_arr[y][x],y*-1,x*-1)
                    if max_loc < temp:
                        max_loc = temp
                player_arr[max_loc[1]*-1][max_loc[2]*-1]+=len(v)
                v=[]
                max_loc = (len(type_arr[max_loc[1]*-1][max_loc[2]*-1])*-1,player_arr[max_loc[1]*-1][max_loc[2]*-1], max_loc[1],max_loc[2])
                group.append(max_loc)
    return sorted(group,reverse=True)

def dinner(group):
    for i in range(len(group)):
        if group[i] == 0:
            continue
        _,value,y,x=group[i]
        y*=-1
        x*=-1
        type = type_arr[y][x]
        dist = value%4
        player_arr[y][x]=1
        b_val = value-1
        d=[(-1,0),(1,0),(0,-1),(0,1)]
        while True:
            dy,dx=d[dist]
            y+=dy
            x+=dx
            if not in_range(y,x) or b_val==0:
                break
            if type != type_arr[y][x] :
                if b_val > player_arr[y][x]:
                    player_arr[y][x]+=1
                    b_val-=player_arr[y][x]
                    type_arr[y][x] = type
                else:
                    player_arr[y][x]+=b_val
                    b_val=0
                    t_len = len(type_arr[y][x])
                    type_arr[y][x]+= type
                    type_arr[y][x] = "".join(dict.fromkeys(type_arr[y][x]))
                    type_fix(y,x)
                    # t_len  len(type_arr[y][x])
                for find_g in range(i+1,len(group)):
                    if (group[find_g][2]*-1,group[find_g][3]*-1) ==(y,x):
                        group[find_g] = 0

def type_fix(pi,pk):
    if type_arr[pi][pk] in ["TCM", "TMC", "CTM", "CMT", "MTC", "MCT"]:
        type_arr[pi][pk] = "TCM"
    elif type_arr[pi][pk] in ["TC", "CT"]:
        type_arr[pi][pk] = "TC"
    elif type_arr[pi][pk] in ["TM", "MT"]:
        type_arr[pi][pk] = "TM"
    elif type_arr[pi][pk] in ["CM", "MC"]:
        type_arr[pi][pk] = "CM"


for i in range(t):
    score = [0] * 7
    morning()
    group = lunch()
    dinner(group)
    for pi in range(n):
        for pk in range(n):
            if type_arr[pi][pk] in ["TCM","TMC","CTM","CMT","MTC","MCT"]:
                type_arr[pi][pk] = "TCM"
                score[0] += player_arr[pi][pk]
            elif type_arr[pi][pk] in ["TC","CT"]:
                type_arr[pi][pk] = "TC"
                score[1] += player_arr[pi][pk]
            elif type_arr[pi][pk] in ["TM","MT"]:
                type_arr[pi][pk] = "TM"
                score[2] += player_arr[pi][pk]
            elif type_arr[pi][pk] in ["CM","MC"]:
                type_arr[pi][pk] = "CM"
                score[3] += player_arr[pi][pk]
            elif type_arr[pi][pk] in ["M"]:
                score[4] += player_arr[pi][pk]
            elif type_arr[pi][pk] in ["C"]:
                score[5] += player_arr[pi][pk]
            elif type_arr[pi][pk] in ["T"]:
                type_arr[pi][pk] = "T"
                score[6] += player_arr[pi][pk]
    for kk in range(len(score)):
        print(score[kk], end=" ")
    print()

    # print(group)
    # for kk in range(n):
    #     print(player_arr[kk])
    # print()
    # #
    # for kk in range(n):
    #     print(type_arr[kk])
    # print()

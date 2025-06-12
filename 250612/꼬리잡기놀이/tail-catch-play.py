import sys
sys.stdin = open("./input.txt")
input = sys.stdin.readline
from collections import deque
n, m, t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
round_arr = []
first_player = []
idx=0
move=0
for i in range(t+1):
    d=[(0,1),(-1,0),(0,-1),(1,0)]
    round_arr.append(d[idx])
    move+=1
    if move ==n:
        move=0
        idx=(idx+1)%4
for i in range(n):
    for k in range(n):
        if arr[i][k] ==1:
            first_player.append([i,k])
def in_range(y,x):
    return x>=0 and x<n and y>=0 and y<n
def move():
    d=[(0,1),(1,0),(0,-1),(-1,0)]
    for i in range(m):
        check=0
        y,x = first_player[i]
        for loc in range(len(d)):
            dy,dx = d[loc]
            oy,ox = dy+y,dx+x
            if in_range(oy,ox) and arr[oy][ox]==4:
                check=1
                visited = [[0]*n for _ in range(n)]
                q=deque()
                q.append((oy,ox))
                visited[oy][ox]=1
                while q:
                    yy,xx= q.popleft()
                    for loc2 in range(len(d)):
                        dy, dx = d[loc2]
                        py, px = dy + yy, dx + xx
                        if in_range(py,px) and visited[py][px]==0 and arr[py][px]!=4 and arr[py][px]!=0:
                            if arr[py][px]==3:
                                arr[py][px]=4
                                arr[py+dy*-1][px+dx*-1] = 3
                            else:
                                arr[py][px] = 2
                                q.append((py,px))
                            visited[py][px] = 1
                arr[oy][ox] = 1
                first_player[i] = [oy, ox]
        if check ==0:
            for loc in range(len(d)):
                dy, dx = d[loc]
                oy, ox = dy + y, dx + x
                if in_range(oy, ox) and arr[oy][ox] == 3:
                    for loc2 in range(len(d)):
                        ty,tx=d[loc2]
                        yo,xo = oy+ty,ox+tx
                        if in_range(yo, xo) and arr[yo][xo] == 2:
                            arr[yo][xo]=3

                    check = 1
                    visited = [[0] * n for _ in range(n)]
                    q = deque()
                    q.append((oy, ox))
                    visited[oy][ox] = 1
                    while q:
                        yy, xx = q.popleft()
                        for loc2 in range(len(d)):
                            dy, dx = d[loc2]
                            py, px = dy + yy, dx + xx
                            if in_range(py, px) and visited[py][px] == 0 and arr[py][px] != 4 and arr[py][px] != 0 and arr[py][px] != 3:
                                arr[py][px] = 2
                                q.append((py, px))
                                visited[py][px] = 1
                    arr[oy][ox] = 1
                    first_player[i] = [oy, ox]
                    # arr[ty][tx]=3



def score(oriy,orix):
    global arr
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q=deque()
    q.append((oriy,orix))
    visited = [[0]*n for _ in range(n)]
    visited[oriy][orix]=1
    temp3=(-1,-1)
    temp1=(-1,-1)
    scoress = 0
    while q:
        y,x = q.popleft()
        for loc in range(len(d)):
            dy, dx = d[loc]
            oy, ox = dy + y, dx + x
            if in_range(oy, ox) and visited[oy][ox]==0 and arr[oy][ox] != 4 and arr[oy][ox] != 0:
                if arr[oy][ox] == 1:
                    temp1 = (oy,ox)
                    scoress = visited[y][x]+1
                    # break
                elif arr[oy][ox] == 3:
                    temp3 = (oy,ox)
                    # scoress = visited[y][x]+1
                else:
                    visited[oy][ox] = visited[y][x]+1
                    q.append((oy,ox))
    if temp3 ==(-1,-1):
        for i in range(len(first_player)):
            if (first_player[i][0],first_player[i][1])==temp1:
                first_player[i]=[oriy,orix]
                arr[oriy][orix]=1
                arr[temp1[0]][temp1[1]]=3
    elif temp1 ==(-1,-1):
        scoress=1
        for i in range(len(first_player)):
            if (first_player[i][0],first_player[i][1])==(oriy,orix):
                first_player[i]=[temp3[0],temp3[1]]
                arr[oriy][orix]=3
                arr[temp3[0]][temp3[1]]=1
    else:
        for i in range(len(first_player)):
            if (first_player[i][0],first_player[i][1])==temp1:
                first_player[i]=[temp3[0],temp3[1]]
                arr[temp3[0]][temp3[1]]=1
                arr[temp1[0]][temp1[1]]=3

    return scoress**2


def start_round(times):
    yy = times%n
    if round_arr[times] == (0,1):
        y,x = yy,0
    elif round_arr[times] == (-1,0):
        y,x = n-1,yy
    elif round_arr[times] == (0,-1):
        y,x = n-1-yy,n-1
    else:
        y,x = 0,n-1-yy
    for i in range(n):
        if arr[y][x] !=4 and arr[y][x] !=0:
            return score(y,x)
        dy,dx=round_arr[times]
        y,x = y+dy,x+dx

    return 0


ans=0
for times in range(t):
    move()
    s=start_round(times)
    ans+=s


print(ans)
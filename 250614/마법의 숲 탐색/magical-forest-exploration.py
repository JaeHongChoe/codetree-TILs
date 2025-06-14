import sys
sys.stdin = open("./input.txt")
input = sys.stdin.readline

n,m,p = map(int,input().split())
players = [list(map(int,input().split())) for _ in range(p)]
n+=3
arr = [[0]*m for _ in range(n)]
exit_arr = set()
from collections import deque

exit_loc = [(-1,0),(0,1),(1,0),(0,-1)]

def check_arr():
    for i in range(0,3):
        for k in range(m):
            if arr[i][k] !=0:
                return False
    return True

def in_range(y,x):
    return x>=0 and x<m and y>=0 and y<n

def check_gol(y,x):## 바로 위 한칸도 체크
    return in_range(y-1,x) and arr[y-1][x]==0\
        and in_range(y,x+1) and arr[y][x+1]==0\
        and in_range(y+1,x) and arr[y+1][x]==0\
        and in_range(y,x-1) and arr[y][x-1]==0\
        and in_range(y-2,x) and arr[y-2][x]==0\
        and in_range(y-1,x+1) and arr[y-1][x+1]==0\
        and in_range(y,x) and arr[y][x]==0\
        and in_range(y-1,x-1) and arr[y-1][x-1]==0


def gol_move(a,exit):
    texit=exit
    start_y,start_x=a
    q= deque()
    q.append((start_y,start_x))
    visited = [[0]*m for _ in range(n)]
    visited[start_y][start_x]=1
    d=[(1,0),(1,-1),(1,1)]
    while q:
        y,x = q.popleft()
        for loc in range(len(d)):
            dy,dx = d[loc]
            oy, ox = dy+y, dx+x
            if check_gol(oy,ox) and visited[oy][ox]==0:
                if loc == 1:    texit= (texit -1)%4
                if loc == 2:    texit=(texit + 1) % 4
                visited[oy][ox]=1
                q.append((oy,ox))
                break
    return y,x,texit

def move_yo(sy,sx):
    q=deque()
    q.append((sy,sx))
    visited = [[0] * m for _ in range(n)]
    visited[sy][sx]=1
    num = 0
    while q:
        y,x = q.popleft()
        for loc in range(len(exit_loc)):
            dy,dx = exit_loc[loc]
            oy,ox = dy+y,dx+x
            if in_range(oy,ox) and arr[oy][ox] !=0 and visited[oy][ox]==0\
                and (arr[oy][ox]==arr[y][x] or (y,x) in exit_arr):
                visited[oy][ox]=visited[y][x]+1
                q.append((oy,ox))
                if num < oy-2:
                    num = oy-2
    return num

ans = 0
for time in range(p):
    start_point_x, exit_play = players[time]
    start_point_x-=1
    start_point_y=1

    y,x,exit_l=gol_move((start_point_y,start_point_x),exit_play)
    #먼저 골렘 초기 위치 그리기.
    arr[y][x]=time+1
    for loc in range(len(exit_loc)):
        dy,dx = exit_loc[loc]
        arr[y+dy][x+dx] = time + 1
        if loc == exit_l:
            exit_arr.add((y+dy,x+dx))
            # arr[y + dy][x + dx] = -1

    ## 배열이 꽉 찼는지 체크
    check = check_arr()
    if not check:
        arr = [[0]*m for _ in range(n)]
        exit_arr=set()
        continue

    ## 정령이동, 모든 칸으로 갈 수 있고 y가 최대로 오게

    score = move_yo(y,x)
    ans+=score

print(ans)
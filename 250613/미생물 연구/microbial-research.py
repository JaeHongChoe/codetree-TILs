import sys
sys.stdin = open("./input.txt")
input = sys.stdin.readline

from collections import deque
n,p = map(int,input().split())
q_arr = [list(map(int,input().split())) for _ in range(p)]
arr = [[0]*n for _ in range(n)]



def in_range(y,x):
    return x>=0 and x<n and y>=0 and y<n

d = [(0,-1),(1,0),(0,1),(-1,0)]
for time in range(p):
    ## 미생물 투입
    sx,sy,ex,ey = q_arr[time]
    for y in range(sy,ey):
        for x in range(sx,ex):
            arr[y][x]=time+1
    #죽은 생물 찾기
    visited= [[0]*n for _ in range(n)]
    check_arr = [0]*p
    un_value_arr =[[0,0] for _ in range(p)]
    idx_arr = [[] for _ in range(p)]
    for i in range(n):
        for k in range(n):
            if arr[i][k] !=0:   un_value_arr[arr[i][k]-1] = [un_value_arr[arr[i][k]-1][0]+1,(arr[i][k]-1)*-1]
            if arr[i][k] != 0 and visited[i][k]==0:
                q=deque()
                check_arr[arr[i][k]-1]+=1
                q.append((i,k))
                visited[i][k]=1
                idx_arr[arr[i][k]-1].append([i,k])
                while q:
                    y,x = q.popleft()
                    for loc in range(len(d)):
                        dy,dx = d[loc]
                        oy,ox = y+dy, x+dx
                        if in_range(oy,ox) and visited[oy][ox]==0 and arr[i][k] == arr[oy][ox]:
                            visited[oy][ox]=1
                            q.append((oy,ox))
                            idx_arr[arr[i][k] - 1].append([oy, ox])
    ## 영역 체크하고 지우기.
    for i in range(p):
        if check_arr[i] > 1:
            un_value_arr[i]=[0,0]
            for k in range(n):
                for j in range(n):
                    if arr[k][j] == i+1:
                        arr[k][j]=0
    new_arr = [[0]*n for _ in range(n)]
    value_arr = sorted(un_value_arr,reverse=True)

    ## 용기 이동
    for i in range(p):
        if value_arr[i][0] ==0:   continue
        val, id = value_arr[i]
        id*=-1
        min_y, min_x = 99999,99999
        for kk in range( len(idx_arr[id])):
            min_y, min_x = min(idx_arr[id][kk][0],min_y), min(idx_arr[id][kk][1],min_x)
        min_y*=-1
        min_x*=-1
        y,x=min_y,min_x
        count=0
        oy,ox=0,0
        while True:
            if count == len(idx_arr[id]):   break
            if oy >= n:
                y = min_y
                x += 1
            if ox >=n:
                y=-99999
                x=-99999
                break
            count = 0
            for k in range(len(idx_arr[id])):
                oy,ox = idx_arr[id][k]
                oy+=y
                ox+=x
                if oy>=n or ox>=n:  break
                if new_arr[oy][ox] !=0:
                    y+=1
                    break
                count += 1

        if (-99999,-99999) != (y,x):
            for k in range(len(idx_arr[id])):
                oy,ox = idx_arr[id][k]
                new_arr[y+oy][x+ox]=id+1
    arr = new_arr

    visited = [[0] * n for _ in range(n)]
    score_set = set()
    for i in range(n):
        for k in range(n):
            if arr[i][k] !=0:
                q= deque()
                q.append((i,k))
                visited[i][k]=1
                while q:
                    y,x = q.popleft()
                    for loc in range(len(d)):
                        dy,dx = d[loc]
                        oy,ox = dy+y,dx+x
                        if in_range(oy,ox) and arr[oy][ox]!=0:
                            if arr[oy][ox] != arr[y][x]:
                                score_set.add((min(arr[oy][ox],arr[y][x]),max(arr[oy][ox],arr[y][x])))
                            if visited[oy][ox]==0:
                                visited[oy][ox]=1
                                q.append((oy,ox))
    ans=0
    for i in range(len(score_set)):
        one,two = score_set.pop()
        ans+=un_value_arr[one-1][0]*un_value_arr[two-1][0]
    print(ans)
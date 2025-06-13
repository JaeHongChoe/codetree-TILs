import sys
sys.stdin = open("./input.txt")
input = sys.stdin.readline

from collections import deque
n,m,t = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

attack = [[0]*m for _ in range(n)]

for time in range(t):
    damaged = [[0] * m for _ in range(n)]
    # 공격자 선언 + 공격대상 선언
    find_attacker = (99999,99999,-1,99999)
    loc_attacker=(-1,-1)

    find_target = (-1,-1,-1,99999)
    loc_target=(-1,-1)

    for i in range(n):
        for k in range(m):
            if arr[i][k] ==0:   continue
            temp_attacker = (arr[i][k],attack[i][k],(i+k)*-1,i*-1)
            temp_target = (arr[i][k], attack[i][k], (i + k)*-1 , i*-1)
            #hunter
            if find_attacker > temp_attacker:
                find_attacker = temp_attacker
                loc_attacker=(i,k)
            #target
            if find_target < temp_target:
                find_target = temp_target
                loc_target=(i,k)
    ## loc 찾았으니 포탑에 공격력 늘려주기
    arr[loc_attacker[0]][loc_attacker[1]] += (n+m)
    ### laseer attack 근데 불가능하면 포탄
    visited= [[0]*m for _ in range(n)]
    visited[loc_target[0]][loc_target[1]] = 1
    q=deque()
    q.append((loc_target[0],loc_target[1]))
    d_l = [(0,1),(1,0),(0,-1),(-1,0)]
    while q:
        y,x = q.popleft()
        for loc in range(len(d_l)):
            dy,dx = d_l[loc]
            oy, ox = y+dy, x+dx
            if oy <0:   oy = n-1
            if oy >=n:  oy=0
            if ox <0:   ox = m-1
            if ox >=n:  ox=0
            if visited[oy][ox]==0 and arr[oy][ox] !=0:
                q.append((oy,ox))
                visited[oy][ox] = visited[y][x]+1
    #visited에 0이 아니면 레이저 공격, 0이면 포탄 공격
    damage = arr[loc_attacker[0]][loc_attacker[1]]
    if visited[loc_attacker[0]][loc_attacker[1]] !=0:
        ay,ax = loc_attacker
        go_navi = (visited[ay][ax],9)
        for i in range(visited[loc_attacker[0]][loc_attacker[1]]):
            for loc in range(len(d_l)):
                dy, dx = d_l[loc]
                oy, ox = ay + dy, ax + dx
                if oy < 0:   oy = n - 1
                if oy >= n:  oy = 0
                if ox < 0:   ox = m - 1
                if ox >= n:  ox = 0
                if visited[oy][ox] !=0:
                    temp = (visited[oy][ox],loc)
                    if go_navi > temp:
                        go_navi = temp
            dy,dx = d_l[go_navi[1]]
            ay+=dy
            ax+=dx
            if ay < 0:   ay = n - 1
            if ay >= n:  ay = 0
            if ax < 0:   ax = m - 1
            if ax >= n:  ax = 0
            if (ay,ax) != loc_target:
                arr[ay][ax] -= damage//2
            else:
                arr[ay][ax] -= damage
            damaged[ay][ax] = 1
            if arr[ay][ax] < 0: arr[ay][ax]=0

    ## 포탄 공격을 해야하는 상황
    else:
        y,x = loc_target
        arr[y][x]-=damage
        damaged[y][x] = 1
        if arr[y][x] < 0: arr[y][x] = 0
        d = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        for loc in range(len(d)):
            dy, dx = d[loc]
            oy, ox = y + dy, x + dx
            if oy < 0:   oy = n - 1
            if oy >= n:  oy = 0
            if ox < 0:   ox = m - 1
            if ox >= n:  ox = 0
            if arr[oy][ox] ==0: continue
            if (oy,ox) == loc_attacker: continue
            arr[oy][ox]-=damage//2
            damaged[oy][ox] = 1
            if arr[oy][ox] < 0: arr[oy][ox] = 0

    ## 공격 시점 체크하기 + 정비도 동시에 진행 + 포탑 1개 남으면 종료 시키기
    cnt=0
    for i in range(n):
        for k in range(m):
            if arr[i][k] !=0:   cnt+=1
            if (i,k) == loc_attacker:   continue
            attack[i][k]+=1
            if damaged[i][k]==0 and arr[i][k]!=0:
                arr[i][k]+=1
    if cnt ==1:
        break

ans = 0
for i in range(n):
    for k in range(m):
        if ans < arr[i][k]:
            ans=arr[i][k]
print(ans)

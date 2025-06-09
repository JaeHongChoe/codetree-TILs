t, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(5)]
m_arr = list(map(int,input().split()))
visited = [[0]*5 for _ in range(5)]
from collections import deque
q= deque()

def in_range(y,x):
    return x >=0 and x <5 and y>=0 and y<5

def bfs(temp_arr):
    d = [(0,-1),(1,0),(0,1),(-1,0)]
    visited = [[0] * 5 for _ in range(5)]
    same = [[0] * 5 for _ in range(5)]
    group=[]
    # q = deque()
    # q.append((0,0))
    # visited[0][0] = 1
    num=0
    cnt=0
    for i in range(5):
        for k in range(5):
            for loc in range(len(d)):
                dy, dx = d[loc]
                oy, ox = dy + i, dx + k
                if in_range(oy, ox) and temp_arr[i][k] == temp_arr[oy][ox] and same[i][k]==0:
                    # same = [[0] * 5 for _ in range(5)]
                    q = deque()
                    q.append((i,k))
                    num += 1
                    same[i][k]=num
                    temp=1
                    while q:
                        y,x = q.popleft()
                        for loc in range(len(d)):
                            dy, dx = d[loc]
                            oy, ox = dy+y , dx+x
                            if in_range(oy,ox) and temp_arr[y][x] == temp_arr[oy][ox] and same[oy][ox]==0:
                                q.append((oy,ox))
                                same[oy][ox]=num
                                temp+=1
                    if temp >=3:
                        cnt+=temp
                        group.append(num)

    return same,cnt,group

def rot90(sy,sx,length,arr):
    temp_arr = [[0] * 5 for _ in range(5)]
    for i in range(sy,sy+length):
        for k in range(sx,sx+length):
            dy, dx = i-sy, k-sx
            oy, ox = dx, length-1-dy
            temp_arr[oy+sy][ox+sx] = arr[i][k]
    for i in range(5):
        for k in range(5):
            if temp_arr[i][k] ==0:
                temp_arr[i][k] = arr[i][k]

    return temp_arr

def find_loc():
    global m_arr
    max_loc = (-1,4,99999,99999)
    visited_t=[]
    group_t=[]
    arr_t=[]
    for ii in range(3):
        for kk in range(3):
            temp_arr = arr
            for times in range(3):
                temp_arr = rot90(ii,kk,3,temp_arr)
                visited,cnt,group = bfs(temp_arr)
                temp_loc = (cnt,times*-1,ii*-1,kk*-1)
                if max_loc < temp_loc:
                    max_loc = temp_loc
                    visited_t=visited
                    group_t=group
                    arr_t=temp_arr
    return max_loc,visited_t,group_t,arr_t

mm_num=0
for times in range(t):
    ans=0
    max_loc, visited, group,arr_t = find_loc()
    if max_loc[0] ==0:
        break
    arr=arr_t
    for i in range(5):
        for k in range(4, -1, -1):
            if visited[k][i] in group:
                # print(k, i)
                arr[k][i] = m_arr[mm_num]
                mm_num += 1
                ans += 1
                # print(cnt, mm_num)
    while True:
        visited, cnt, group = bfs(arr)
        if cnt ==0:
            break
        for i in range(5):
            for k in range(4, -1, -1):
                if visited[k][i] in group:
                    arr[k][i] = m_arr[mm_num]
                    mm_num += 1
                    ans += 1

    print(ans,end=" ")

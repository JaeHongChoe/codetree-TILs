m, n = map(int,(input().split()))
arr = [list(map(int,(input().split()))) for _ in range(m)]
movement = [list(map(int,(input().split()))) for _ in range(n)]
visited = [[0]*m for i in range(m)]
visited[m-1][0:2] = 1, 1
visited[m-2][0:2] = 1, 1

def in_range(y,x):
    return x >=0 and x <= m-1 and y >= 0 and y <= m-1

def sim(move):
    global arr,visited
    d = [(0,0),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]
    d_idx, time = move
    temp_visited = [[0]*m for i in range(m)]
    for i in range(m):
        for k in range(m):
            if visited[i][k] == 1:
                ry, rx = d[d_idx]
                ry = (ry * time + i + m*time)%m
                rx = (rx * time + k + m*time)%m
                # for _ in range(time):
                #     ry += d[d_idx][0]
                #     rx += d[d_idx][1]
                # if not in_range(ry,rx):
                #     ry = abs(ry)%m
                #     rx = abs(rx)%m
                temp_visited[ry][rx] = 1
                arr[ry][rx] += 1
    for i in range(m):
        for k in range(m):
            if temp_visited[i][k] == 1:
                cnt = 0
                for j in [2,4,6,8]:
                    oy,ox = d[j]
                    oy,ox = oy + i, ox + k
                    if in_range(oy,ox) and arr[oy][ox] >0:
                        cnt +=1
                arr[i][k] += cnt
    # print(temp_visited)    
    for i in range(m):
        for k in range(m):
            if temp_visited[i][k] == 0 and arr[i][k] >= 2:
                arr[i][k] -=2
                temp_visited[i][k] = 1
            elif temp_visited[i][k] == 1:
                temp_visited[i][k] = 0
    visited = temp_visited
    # print(arr,visited)

for move in movement:
    sim(move)
    # print(arr, move)
    # print(visited)
ans = 0
# print(arr)
for i in range(m):
    ans +=sum(arr[i])
print(ans)
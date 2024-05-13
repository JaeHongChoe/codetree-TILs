a = int(input())

graph = [
    list(map(int,input().split()))
    for _ in range(a)
]

visited = [
    [0 for _ in range(a)]
    for _ in range(a)
]

ans = []

def in_range(x, y):
    return 0 <= x and x < a and 0 <= y and y < a

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or graph[x][y] ==0:
        return False
    return True


def dfs(x,y):
    global cnt
    # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
    dxs, dys = [1,0,-1,0],[0,-1,0,1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            visited[new_x][new_y] =1
            cnt +=1
            dfs(new_x,new_y)
            

for i in range(a):
    for k in range(a):
        if can_go(i, k):
            visited[i][k] =1
            cnt =1
            dfs(i,k)
            ans.append(cnt)
        

print(len(ans))
for k in sorted(ans):
    print(k)
a,b = map(int,input().split())

graph = [
    list(map(int,input().split()))
    for _ in range(a)
]

visited = [
    [0 for _ in range(b)]
    for _ in range(a)
]

ans = [
    [0 for _ in range(b)]
    for _ in range(a)
]

def in_range(x,y):
    return 0 <= x and x <a and 0 <= y and y < b

def can_go(x, y):
    if not in_range(x,y):
        return False
    if visited[x][y] or graph[x][y] ==0:
        return False
    return True

def dfs(x, y):
    global order

    dxs, dys = [1,0],[0,1]

    for dx,dy in zip(dxs, dys):
        new_x, new_y = dx + x, dy + y
        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            ans[new_x][new_y] = 1
            dfs(new_x, new_y)


ans[0][0] = 1
visited[0][0]=1
dfs(0,0)
print(ans[-1][-1])
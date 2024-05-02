a,b = map(int,input().split())
order =1
graph =[
    list(map(int,input().split()))
    for _ in range(a)
]

ans =[
    [0 for _ in range(a)]
    for _ in range(a)
]

visited =[
    [0 for _ in range(a)]
    for _ in range(a)
]

def in_range(x,y):
    return 0 <= x and x < a and 0 <= y and y<a

def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if visited[x][y] or graph[x][y] ==0:
        return False
    return True

def dfs(x,y):
    global order,visited
    
    dxs, dys = [1,0],[0,1]
    

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy

        if can_go(new_x, new_y):
            ans[new_x][new_y] = order
            order +=1
            visited[new_x][new_y] =1
            dfs(new_x,new_y)
    return visited

ans[0][0] = order
order +=1
visited[0][0] = 1

visited = dfs(0,0)
if visited[-1][-1] == 0:
    print(0)
else:
    print(1)
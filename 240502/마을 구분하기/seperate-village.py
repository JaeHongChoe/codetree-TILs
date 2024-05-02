a = int(input())

grid = [
    list(map(int,input().split()))
    for _ in range(a)
]

visited = [
    [0 for _ in range(a)]
    for _ in range(a)
]

ans= []

def in_range(x,y):
    return 0 <= x and x < a and 0 <= y and y < a

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x,y):
    global cnt

    dxs, dys = [0,1,0,-1], [1,0,-1,0]

    for dx, dy in zip(dxs,dys):
        new_x, new_y = x +dx, y+dy

        if can_go(new_x,new_y):
            cnt+=1
            visited[new_x][new_y] =1
            dfs(new_x,new_y)


temp=0
for k in range(a):
    for j in range(a):
        if can_go(k,j):
            visited[k][j] = 1
            cnt = 1
            dfs(k,j)
            ans.append(cnt)
            temp +=1
            
ans.sort()
print(len(ans))
for k in ans:
    print(k)
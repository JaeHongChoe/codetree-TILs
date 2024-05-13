a, b = map(int,input().split())


# graph = [
#     list(map(int,input().split()))
#     for _ in range(b)
# ]

# visited = [
#     [0 for _ in range(a + 1)]
#     for _ in range(b)
# ]
graph = [[] for _ in range(a+1)]
visited = [False for _ in range(a+1)]

def dfs(vertex):
    global cnt
    for kk in graph[vertex]:
        if not visited[kk]:
            # print(kk)
            visited[kk] = True
            dfs(kk)
            cnt+=1


for _ in range(b):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
cnt=0
visited[1]= True
dfs(1)
print(cnt)
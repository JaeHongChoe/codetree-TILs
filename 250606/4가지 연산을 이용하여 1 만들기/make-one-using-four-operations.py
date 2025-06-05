N = int(input())
# arr = [i+1 for i in range(1000000)]
visited = [0 for i in range(1000000)]
# print(arr)

def push(n,s):
    visited[n] = s

def bfs():
    d =[(1),(-1),(2),(3)]
    n=-1
    while n!=1:
        n=q.popleft()
        for i in range(4):
            on = n
            if i ==0:
                on+=1
            elif i ==1:
                on-=1
            elif i ==2:
                if on%2==0:
                    on= int(on/2)
            elif i ==3:
                if on%3==0:
                    on= int(on/3)
            if on >=1 and on < 1000000 and visited[on]==0:
                push(on,visited[n]+1)
                q.append(on)
    # print(visited)
    print(visited[1]-1)
from collections import deque
q=deque()
q.append(N)
visited[N] = 1
bfs()
# Please write your code here.
# 10 9 3 1
# 10 5 4 2 1
# 10 5 6 2 1
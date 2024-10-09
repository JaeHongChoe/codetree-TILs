import heapq

n, m = list(map(int,input().split()))
pq = []
for _ in range(n):
    x,y = list(map(int,input().split()))
    heapq.heappush(pq, ((x+y),x,y))
    
for _ in range(m):
    _,x,y = heapq.heappop(pq)
    x+=2
    y+=2
    heapq.heappush(pq, ((x+y),x,y))
    
_, x,y = heapq.heappop(pq)
print(x,y)
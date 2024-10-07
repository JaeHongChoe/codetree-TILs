import heapq

count, dist = list(map(int,input().split()))

pq = []
arr = list(map(int,input().split()))

for i in arr:
    heapq.heappush(pq,-i)

for _ in range(dist):
    temp = -heapq.heappop(pq)
    heapq.heappush(pq,-(temp-1))
print(-pq[0])
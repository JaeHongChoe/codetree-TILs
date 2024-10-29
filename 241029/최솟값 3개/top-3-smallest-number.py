import heapq
n = int(input())
lists = list(map(int,input().split()))
pq = []

for i in range(n):
    if i <2:
        print(-1)
        heapq.heappush(pq,lists[i]*-1)
    else:
        if i ==2:
            heapq.heappush(pq,lists[i]*-1)
        elif pq[0] < lists[i]*-1:
            heapq.heappop(pq)
            heapq.heappush(pq,lists[i]*-1)
        print((pq[0]*pq[1]*pq[2])*-1)
import heapq

count = int(input())
pq = []
for _ in range(count):
    x = int(input())

    if x == 0:
        if len(pq) == 0:
            print(0)
        else:
            print(-(heapq.heappop(pq)))
    else:
        heapq.heappush(pq,-x)
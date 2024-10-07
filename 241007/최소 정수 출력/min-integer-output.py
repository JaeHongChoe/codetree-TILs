import heapq

count = int(input())
pq = []
for _ in range(count):
    temp = int(input())

    if temp == 0:
        if len(pq) ==0:
            print(0)
        else:
            print(heapq.heappop(pq))
    else:
        heapq.heappush(pq,temp)
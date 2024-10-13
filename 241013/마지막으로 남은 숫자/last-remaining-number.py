import heapq

count = int(input())

arr_list = list(map(int,input().split()))
pq =[]
for i in range(count):
    heapq.heappush(pq,-arr_list[i])

while(True):
    first = heapq.heappop(pq)
    second = heapq.heappop(pq)
    temp = second - first
    if temp != 0:
        heapq.heappush(pq,-temp)
    if len(pq) == 1:
        print(-heapq.heappop(pq))
        break
    elif len(pq) == 0:
        print(-1)
        break
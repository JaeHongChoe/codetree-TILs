import heapq
count = int(input())
arr_list = list(map(int,input().split()))

pq_max = []
pq_min = []

for i in range(count):
    heapq.heappush(pq_max, -arr_list[i])
    heapq.heappush(pq_min, arr_list[i])


for i in range(count):
    if arr_list[i] == -heapq.heappop(pq_max):
        temp = sum(arr_list[i-1:])
        length = len(arr_list[i-1:])
        if length > 2:
            temp -= min(arr_list[i-1:])
            length -= 1
        print(f"{temp/length:.2f}")
        break
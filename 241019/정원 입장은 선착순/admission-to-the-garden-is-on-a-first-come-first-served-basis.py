import heapq
n = int(input())
pq=[]
ans = []
stay_list = []
for i in range(n):
    temp = list(map(int,input().split()))
    heapq.heappush(pq,(temp+[i]))
    # print(pq)
start, stay,_ = heapq.heappop(pq)
end = start +stay
# print(pq)

while(pq):
    start, stay,idx = heapq.heappop(pq)
    if start < end:
        heapq.heappush(stay_list, [idx,start,stay])
    elif stay_list:
        idx, start, stay = heapq.heappop(stay_list)
        heapq.heappush(ans, [(end-start)*-1,idx])
        end = end + stay
        # print(ans)
time,_ = heapq.heappop(ans)
print(time*-1)
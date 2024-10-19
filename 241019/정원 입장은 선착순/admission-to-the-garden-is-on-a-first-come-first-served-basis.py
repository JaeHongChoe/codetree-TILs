import heapq
n = int(input())
pq=[]
ans = []
stay_list = []
for i in range(n):
    a, b = list(map(int,input().split()))
    heapq.heappush(pq,[a,i,b])
    # print(pq)
start, _,stay = heapq.heappop(pq)
end = start +stay
# print(pq)

while(True):
    if not pq and not stay_list:
        break
    while(True):
        if pq:
            start, idx,stay = heapq.heappop(pq)
        else:
            break
        if start < end:
            heapq.heappush(stay_list, [idx,start,stay])
            # print(stay_list,"fdsaf")
        else:
            break
        # elif start > end or not pq:
        #     break
    if stay_list:
        idx, start, stay = heapq.heappop(stay_list)
        heapq.heappush(ans, [(end-start)*-1,idx])
        end = end + stay
        # print(ans)
    # else:

time,_ = heapq.heappop(ans)
print(time*-1)
import heapq
n = int(input())
pq = []
for _ in range(n):
    m = int(input())
    if m < 0:
        heapq.heappush(pq, (m*-1,0))
    elif m > 0:
        heapq.heappush(pq, (m,1))
    else:
        if pq:
            ans,stat = heapq.heappop(pq)
            if stat ==0:
                ans = ans*-1
            print(ans)
        else:
            print(0)
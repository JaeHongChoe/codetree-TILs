import heapq
n, m, k = list(map(int,input().split()))
pq =[]
n_arr = list(map(int,input().split()))
m_arr = list(map(int,input().split()))
n_arr = sorted(n_arr)
m_arr = sorted(m_arr)


for i in range(n):
    heapq.heappush(pq, (n_arr[i] + m_arr[0], i, 0))

for i in range(k-1):
    _, idx1, idx2 = heapq.heappop(pq)
    idx2 += 1
    if idx2 < m:
        heapq.heappush(pq, (n_arr[idx1]+m_arr[idx2],idx1,idx2))

sum_,_,_ = heapq.heappop(pq)
print(sum_)
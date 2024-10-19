import heapq
n, m, k = list(map(int,input().split()))
pq =[]
n_arr = list(map(int,input().split()))
m_arr = list(map(int,input().split()))

n_visit = [0] * len(n_arr)
m_visit = [0] * len(m_arr)

def permutations(n, new_arr):
    global arr
    # 순서 상관 0, 중복 X
    if len(new_arr) == n:
        heapq.heappush(pq,sum(new_arr))
        return
    for i in range(len(n_arr)):
        if not n_visit[i]:
            n_visit[i] = 1
            for k in range(len(m_visit)):
                if not m_visit[k]:
                    m_visit[k] = 1
                    permutations(n, [n_arr[i]] + [m_arr[k]])
                    m_visit[k] = 0
            n_visit[i] = 0

permutations(2, [])
for _ in range(k):
    ans = heapq.heappop(pq)
print(ans)
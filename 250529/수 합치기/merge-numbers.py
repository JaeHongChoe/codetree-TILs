import heapq

# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))

pq = []
ans = 0


# 우선순위 큐에 원소들을 전부 넣어줍니다.
# 작은 숫자 2개를 골라 합치는 것이 항상 유리함을 이용해야 하므로
# 작은 숫자가 먼저 골라질 수 있도록 해야합니다.
for elem in arr:
    heapq.heappush(pq, elem)

# 원소가 2개 이상이면 계속
# 가장 작은 숫자 2개를 골라
# 합치는 것을 반복합니다.
while len(pq) > 1:
    x1 = heapq.heappop(pq)
    x2 = heapq.heappop(pq)

    # 가장 작은 숫자 2개를 더하기 위한 비용을 답에 더해주고,
    # 두 숫자를 합친 결과를 우선순위 큐에 다시 넣어줍니다.
    ans += (x1 + x2)
    heapq.heappush(pq, x1 + x2)

print(ans)

N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)
price = []
ans = 0
for i in range(N):
    price.append([v[i]/w[i],i])
price = sorted(price,reverse=True)
for i in range(N):
    val , loc = price[i][0], price[i][1]
    if M - w[loc] >=0:
        ans += v[loc]
        M -=w[loc]
    else:
        ans = ans + M*val
        break
print("{:.3f}".format(ans))
# Please write your code here.

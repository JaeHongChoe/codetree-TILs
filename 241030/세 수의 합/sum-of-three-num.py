n, m = list(map(int,input().split()))
lists = list(map(int,input().split()))
d = dict()
ans = 0

for i in range(n):
    if lists[i] not in d:
        d[lists[i]] = 1
    else:
        value = d[lists[i]] 
        d[lists[i]] = value + 1

for i in range(n):
    d[lists[i]] -= 1
    for t in range(i):
        temp = m - lists[i] - lists[t]
        if temp in d:
            ans += d[temp]
            # print(d)
print(ans)
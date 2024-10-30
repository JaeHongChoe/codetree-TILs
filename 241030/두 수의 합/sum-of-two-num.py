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
    if m - lists[i] in d:
        ans += d[m - lists[i]]
print(ans)
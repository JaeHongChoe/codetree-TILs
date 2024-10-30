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
    if m - lists[i] in d:
        t1 = d.pop(lists[i])
        t2 = d.pop(m - lists[i])
        ans += t1 * t2
print(ans)
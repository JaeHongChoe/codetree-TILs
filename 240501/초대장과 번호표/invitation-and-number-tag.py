a, b = map(int,input().split())
inv = [
    list(map(int,input().split()))
    for _ in range(b)
]
ans = set()
ans.add(1)

for k in inv:
    if k[1] in ans and k[0] - len(ans) <= 1:
        for j in k[1:]:
            ans.add(j)
    else:
        ans.add(k[1])

print(len(ans))

# print(a,b,inv,ans)
a = int(input())
b = [

    list(map(int,input().split()))
    for _ in range(a)
]

dic ={}
ans =0
for k in b:
    if k[0] not in dic:
        dic[k[0]] = k[1]
        ans += k[1]
    elif dic[k[0]] > k[1]:
        ans += k[1] - dic[k[0]]
        dic[k[0]] =k[1]

print(ans)
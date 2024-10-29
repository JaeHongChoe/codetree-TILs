n = int(input())

d = dict()
ans = 0
for _ in range(n):
    temp = input()
    if temp not in d:
        d[temp] = 1
        value =0
    else:
        value = d[temp]
        d[temp] = value+1
    if ans < value+1:
        ans = value+1
print(ans)
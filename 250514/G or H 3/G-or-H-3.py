n, k = map(int, input().split())
x = []
c = []
ans = 0
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)
temp = sorted(x)
for i in temp:
    if c[x.index(i)] == "G":
        l = 1
    else:
        l = 2
    if  l + ans < k:
        ans += l
print(ans)
# Please write your code here.
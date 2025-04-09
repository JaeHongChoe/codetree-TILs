n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

grid = [[0]*max(x2)for _ in range(max(y2))]
ans = 0
for j in range(n):
    for i in range(y1[j],y2[j]):
        for k in range(x1[j],x2[j]):
            if grid[i][k] == 0:
                grid[i][k] = 1
                ans +=1

print(ans)
# Please write your code here.
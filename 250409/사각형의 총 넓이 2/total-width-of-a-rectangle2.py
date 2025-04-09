n = int(input())
x1, y1, x2, y2 = [], [], [], []
offset = 100
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a+offset)
    y1.append(b+offset)
    x2.append(c+offset)
    y2.append(d+offset)

grid = [[0]*200for _ in range(200)]
ans = 0
for j in range(n):
    for i in range(y1[j],y2[j]):
        for k in range(x1[j],x2[j]):
            if grid[i][k] == 0:
                grid[i][k] = 1
                ans +=1

print(ans)
# Please write your code here.
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for k in range(n-2):
        temp = sum(grid[i][k:k+3])
        if ans < temp:
            ans = temp
print(ans)
# Please write your code here.
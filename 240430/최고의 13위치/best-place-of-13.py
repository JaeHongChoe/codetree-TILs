a = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(a)
]

ans =0

for k in range(a):
    for j in range(a-2):
        ans = max(ans, sum(grid[k][j:j+3]))

print(ans)
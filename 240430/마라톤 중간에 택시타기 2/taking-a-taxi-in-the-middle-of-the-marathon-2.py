a = int(input())
grid =[
    list(map(int,input().split()))
    for _ in range(a)
]
min_range = 9999999
for k in range(1,a-1):
    temp = abs(grid[0][0] - grid[k][0]) + abs(grid[0][1] - grid[k][1])
    temp2 = abs(grid[-1][0] - grid[k][0]) + abs(grid[-1][1] - grid[k][1])
    total = temp+temp2
    
    min_range = min(min_range, total)

print(min_range)
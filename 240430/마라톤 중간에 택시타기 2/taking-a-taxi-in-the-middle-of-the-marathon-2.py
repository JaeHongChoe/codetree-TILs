a = int(input())
grid =[
    list(map(int,input().split()))
    for _ in range(a)
]
min_range = 9999999
for k in range(1,a-1):
    dist=0
    prev_idx=0
    for j in range(1, a):
        if j == k:
            continue
        dist += abs(grid[prev_idx][0] - grid[j][0]) + abs(grid[prev_idx][1] - grid[j][1])
        prev_idx = j
    
    min_range = min(min_range, dist)

print(min_range)
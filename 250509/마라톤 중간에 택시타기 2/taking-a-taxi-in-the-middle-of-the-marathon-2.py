n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

total = 9999999
point = [0,0]
point[0] = abs(points[0][0] - points[1][0])
point[1] = abs(points[0][1] - points[1][1])



for i in range(1,n-1):
    ans = 0
    point[0] = points[0][0]
    point[1] = points[0][1]

    for k in range(1,n-1):
        if i == k:
            continue
        ans += abs(point[0] - points[k][0]) + abs(point[1] - points[k][1])
        point[0] = points[k][0]
        point[1] = points[k][1]

    ans += abs(point[0] - points[-1][0]) + abs(point[1] - points[-1][1])
    if total > ans:
        total = ans

print(total)
# Please write your code here.
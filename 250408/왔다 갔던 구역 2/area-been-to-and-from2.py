n = int(input())
# x = []
# dir = []
line = {}
status_1 = 0
status_2 = 0
for _ in range(n):
    xi, di = input().split()
    if di == "R":
        status_1 += int(xi)
        for i in range(status_2, status_1,1):
            if i in line:
                line[i] +=1
            else:
                line[i] = 1
        status_2 = status_1
    else:
        status_1 -= int(xi)
        for i in range(status_1, status_2,1):
            if i in line:
                line[i] +=1
            else:
                line[i] = 1
        status_2 = status_1
ans = 0
for i in line.values():
    if i >=2:
        ans += 1
print(ans)
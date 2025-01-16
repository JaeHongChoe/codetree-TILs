n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

temp = [0 for _ in range(n)]

for left,right in commands:
    cnt = 1 + (right - left)
    for i in range(cnt):
        temp[i+left-1] += 1
print(max(temp))
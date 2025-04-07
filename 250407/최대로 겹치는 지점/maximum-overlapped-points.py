n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

line = {}

for i,j in segments:
    for k in range(i,j+1,1):
        if k in line:
            line[k] += 1
        else:
            line[k] =1
print(max(line.values()))
# Please write your code here.
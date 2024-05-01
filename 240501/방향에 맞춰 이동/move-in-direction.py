dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
a = int(input())
x,y = 0,0
for _ in range(a):
    m, n = map(str,input().split())
    n = int(n)
    if m in 'N':
        x +=  dx[3] * n
        y += dy[3]* n
    elif m in 'E':
        x +=  dx[0]* n
        y +=  dy[0]* n
    elif m in 'S':
        x +=  dx[1]* n
        y += dy[1]* n
    else:
        x +=  dx[2]* n
        y +=  dy[2]* n

print(x,y)
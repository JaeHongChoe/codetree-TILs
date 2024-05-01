from collections import deque

a = int(input())
b = [
    list(map(str,input().split()))
    for _ in range(a)
]

dq = deque()

for k in b:
    # print(k[0])
    if k[0] in 'push':
        dq.append(int(k[1]))
    elif k[0] in 'empty':
        print(int(not dq))
    elif k[0] in 'size':
        print(len(dq))
    elif k[0] in 'pop':
        print(dq.popleft())
    else:
        print(dq[0])
count = int(input())

togo = [
    list(map(str,input().split()))
    for _ in range(count)
]

x=0
y=0
ans =0
kill=0
for i in range(count):
    cnt = int(togo[i][1])
    if kill:
        break
    if togo[i][0] == 'N':
        for j in range(cnt):
            y+=1
            ans+=1
            if x ==0 and y ==0:
                kill =1
                break
    elif togo[i][0] == 'E':
        for j in range(cnt):
            x+=1
            ans+=1
            if x ==0 and y ==0:
                kill = 1
                break
    elif togo[i][0] == 'S':
        for j in range(cnt):
            y-=1
            ans+=1
            if x ==0 and y ==0:
                kill = 1
                break
    elif togo[i][0] == 'W':
        for j in range(cnt):
            x-=1
            ans+=1
            if x ==0 and y ==0:
                kill =1
                break

print(ans)
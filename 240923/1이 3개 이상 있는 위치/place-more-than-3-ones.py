a = int(input())
grid =[
    list(map(int,input().split()))
    for _ in range(a)
]
# 서 남 동 북
ans=0
d = [(0,-1),(1,0),(0,1),(-1,0)]
def in_range(x,y):
    return 0<=x and x <a and 0<=y and y<a
for i in range(a):
    for j in range(a):
        cnt=0
        for idx in range(len(d)):
            dx, dy = j + d[idx][1],i + d[idx][0]
            if in_range(dx,dy) and grid[dx][dy] ==1:
                cnt +=1
        if cnt >=3:
            ans+=1


print(ans)
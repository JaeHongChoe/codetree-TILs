a = int(input())
b = list(map(int,input().split()))

b.sort()

ans = sum(b)
old =[]
while(True):
    temp=[]
    for k in range(0,a,2):
        temp.append(b[k]+b[k+1])
    old = temp
    ans += sum(old)
    if len(old) ==2:
        break
print(ans)
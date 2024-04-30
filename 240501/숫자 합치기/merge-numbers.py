a = int(input())
b = list(map(int,input().split()))

b.sort()

ans = 0
check=0
old =[]
if len(b) %2 !=0:
    check=1
    ans+=b[-1]
while(True):
    temp=[]
    for k in range(0,a-check,2):
        ans+=(b[k]+b[k+1])
        temp.append(b[k]+b[k+1])
    old = temp
    ans += sum(old)
    if len(old) <=2:
        break
print(ans)
a,b = map(int,input().split())
n = list(map(int,input().split()))
dic={}
ans=0
for k in n:
    if k not in dic:
        dic[k] =1
    else:
        dic[k] +=1

for k in n:
    if abs(k-b) not in dic:
        continue
    
    ans += min(dic[abs(k-b)], dic[k] )
    dic.pop(k)
    dic.pop(abs(k-b))


print(ans)
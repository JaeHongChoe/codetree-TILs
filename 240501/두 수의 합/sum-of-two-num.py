a,b = map(int,input().split())
n = list(map(int,input().split()))
dic={}
ans=0
for k in n:
    if k not in dic:
        dic[k] =1
    else:
        dic[k] +=1

for k in set(n):
    if (b-k) not in dic:
        continue
    elif b-k ==k:
        ans += int(dic[k]) * (int(dic[k])-1)
        continue
    
    ans += (dic[(b-k)]* dic[k])

print(ans//2)
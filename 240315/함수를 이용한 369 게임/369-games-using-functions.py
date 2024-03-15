n,m = map(int,input().split())
ans =0

for k in range(n,m+1):
    if k %3 ==0:
        ans +=1
        continue
        
    for i in range(len(str(k))):
        if str(k)[i] in ["3","6","9"]:
            ans+=1
            break
print(ans)
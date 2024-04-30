a = list(input())
ans=0
for k in range(len(a)):
    if a[k] =='(':
        for n in a[k:]:
            if n == ')':
                ans+=1

            
print(ans)
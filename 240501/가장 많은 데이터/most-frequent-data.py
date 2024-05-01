a = int(input())
n = [
    input()
    for _ in range(a)
]

dic ={}
ans =0
for k in n:
    
    if k not in dic:
        dic[k] =1
    else:
        dic[k] += 1
        if ans < dic[k]:
            ans=dic[k]
    

print(ans)
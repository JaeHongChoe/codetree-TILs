n = list(map(int,input().split()))
n_l=[]
ans =0
for i in range(2):
    for k in range(1,n[i]+1,1):
        if n[i] %k ==0 and i ==0:
            n_l.append(k)
        else:
            if n[i] %k ==0 and k in n_l:
                ans = k



print(ans)
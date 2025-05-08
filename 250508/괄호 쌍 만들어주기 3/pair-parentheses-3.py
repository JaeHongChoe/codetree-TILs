A = input()
leng = len(A)
ans = 0
for i in range(leng):
    if A[i] == "(":
        for k in range(i+1,leng):
            if A[k] == ")":
                ans +=1
print(ans)
        
# Please write your code here.
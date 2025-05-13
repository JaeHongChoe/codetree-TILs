A = input()
ans = 0
for i in range(len(A)-3):
    if A[i] == "(" and A[i+1] == "(":
        for k in range(i+2,len(A)-1):
            if A[k] == ")" and A[k+1] == ")":
                ans +=1
print(ans)

# Please write your code here.
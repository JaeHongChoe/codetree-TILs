N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(N):
    for k in range(i+1,N):
        for j in range(k+1,N):
            if A[i] < A[k] and A[k] < A[j]:
                ans+=1
print(ans)
# Please write your code here.
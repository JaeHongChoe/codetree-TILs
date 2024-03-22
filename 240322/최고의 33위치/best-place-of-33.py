n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)] 
ans =0

for d in range(0,n-2,1):
    for r in range(1,n-1,1):
        temp=0
        temp = sum(matrix[d][r-1:r+2]) + sum(matrix[d+1][r-1:r+2]) +sum(matrix[d+2][r-1:r+2])
        if ans < temp:
            ans = temp
print(ans)
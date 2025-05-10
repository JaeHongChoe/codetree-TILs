n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for k in range(n-2):
        temp1 = arr[i][k] + arr[i][k+1] + arr[i][k+2]
        for j in range(i+1,n):
            for m in range(n-2):
                temp2 = arr[j][m] + arr[j][m+1] + arr[j][m+2]
                if ans < temp1 + temp2:
                    ans = temp1 + temp2
print(ans)

# Please write your code here.
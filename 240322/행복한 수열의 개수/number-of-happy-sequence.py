n,m = map(int,input().split())

matrix = [list(map(int, input().split())) for _ in range(n)] 
ans =0

for k in range(n):
    temp =[]
    if len(set(matrix[k])) > m:
        ans +=1
    for d in range(n):
        if len(temp) >m:
            ans +=1 
            break
        if matrix[d][k] not in temp:
            temp.append(matrix[d][k])

print(ans)
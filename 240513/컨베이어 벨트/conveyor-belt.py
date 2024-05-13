a,b = map(int,input().split())

grid = [
    list(map(int,input().split()))
    for _ in range(2)
]
ans =[]
grid = sum(grid,[])

if a*2 < b:
    if b//(a*2) >0:
        temp = b//(a*2)
    b = b - a*2*temp

new_b = a*2 - b
ans.extend(grid[new_b:])
ans.extend(grid[:new_b])

for k in range(1,len(ans)+1):
    print(ans[k-1], end = " ")
    if k % a ==0 :
        print()
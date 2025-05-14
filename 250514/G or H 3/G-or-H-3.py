n, k = map(int, input().split())
x = []
c = []
ans = 0
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)
temp = sorted(x)

def sum_result(i):
    if c[x.index(i)] == "G":
        return 1
    else:
        return 2

for i in range(n):
    l = sum_result(temp[i])
    for j in range(i+1,n):
        if (temp[j] - temp[i]) <= k:
            l += sum_result(temp[j])
        else:
            break
    if ans < l:
        ans = l
            
print(ans)
# Please write your code here.
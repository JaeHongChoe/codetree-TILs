n = int(input())
a = list(map(int, input().split()))
summ = 0
ans = -999999
for i in range(n):
    summ += a[i]
    ans = max(ans,summ)
    if summ <0:
        summ = 0
print(ans)

# Please write your code here.

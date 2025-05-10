n = int(input())
a = [int(input()) for _ in range(n)]
ans = 999999999

for i in range(n):
    temp = 0
    cnt = 0
    for k in range(i,n):
        temp += a[k] * cnt
        cnt += 1
    for j in range(0,i):
        temp += a[j] * cnt
        cnt += 1
    if ans > temp:
        ans = temp
print(ans)
# Please write your code here.

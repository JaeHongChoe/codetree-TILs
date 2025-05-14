N, H, T = map(int, input().split())
arr = list(map(int, input().split()))
ans = 9999999

for i in range(N-T+1):
    temp = 0
    for k in arr[i:T+i]:
        temp += abs(T - k)
    if ans > temp:
        ans = temp
print(ans)

# Please write your code here.
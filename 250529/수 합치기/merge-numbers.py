n = int(input())
arr = list(map(int, input().split()))
tmp = arr[0]
ans = 0

for i in range(1,n-1):
    if tmp < arr[i+1]:
        tmp += arr[i]
        ans += tmp
    else:
        arr[1+i] = arr[1+i] + arr[i]
        ans += arr[1+i]

print(ans+tmp+arr[-1])
# Please write your code here.

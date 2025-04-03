n = int(input())
nums = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    if ans < nums[i] + nums[-i-1]:
        ans = nums[i] + nums[-i-1]
print(ans)

# Please write your code here.

n = int(input())
numbers = list(map(int, input().split()))
ans = 0
for i in range(n):
    for k in range(i+2,n):
        if ans < numbers[i] + numbers[k]:
            ans = numbers[i] + numbers[k]
print(ans)

# Please write your code here.
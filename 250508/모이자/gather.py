n = int(input())
A = list(map(int, input().split()))
cnt = 0
ans = []
for i in range(n):
    temp = cnt +1
    sum_ = 0
    for k in range(n):
        temp -= 1
        sum_ += A[k] * abs(temp)
    ans.append(sum_)
    cnt +=1
print(min(ans))


# Please write your code here.
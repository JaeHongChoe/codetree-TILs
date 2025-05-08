a = input()
ans = 0
for i in range(len(a)):
    temp = list(a)
    temp[i] = abs(int(temp[i])-1)
    sum_temp = 0
    for i in range(len(a)):
        sum_temp = sum_temp *2 + int(temp[i])
    if ans < sum_temp:
        ans = sum_temp
print(ans)
# Please write your code here.
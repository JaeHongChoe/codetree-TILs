a, b = map(int, input().split())
ans =0
while a != b+1:
    if a % 2 !=0 and a % 3 !=0 and a % 5 !=0 and a % 7 !=0:
        temp = a // 10 + a % 10
        if temp % 2 ==0:
            ans +=1
    a +=1
print(ans)
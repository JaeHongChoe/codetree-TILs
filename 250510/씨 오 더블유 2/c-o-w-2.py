n = int(input())
str = input()
ans = 0
for i in range(n):
    if str[i] == "C":
        for k in range(i+1,n):
            if str[k] == "O":
                for j in range(k+1, n):
                    if str[j] == "W":
                        ans +=1
print(ans)

# Please write your code here.
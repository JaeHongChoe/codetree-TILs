a = int(input())
b = list(map(int,input().split()))
total =[]
for k in range(a):
    temp=0
    cnt=k
    for n in range(a):
        if n == k:
            continue
        temp += b[n]* abs(n -cnt)
    total.append(temp)

print(min(total))
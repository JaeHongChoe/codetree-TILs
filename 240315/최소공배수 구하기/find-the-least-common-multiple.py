n = list(map(int,input().split()))

for k in range(max(n[0],n[1]), (n[0]*n[1])):
    if k%n[0] ==0 and k%n[1] ==0:
        print(k)
        break
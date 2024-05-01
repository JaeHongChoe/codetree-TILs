a, b = tuple(map(int, input().split()))
n = list(map(int, input().split()))

dic = dict()

ans = 0


for k in range(a):
    for j in range(k+1,a):
        for p in range(j+1,a):
            if n[k] + n[j] +n[p] == b:
                ans+=1



print(ans)
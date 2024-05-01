a,b = map(int,input().split())
n = list(map(int,input().split()))
m = list(map(int,input().split()))

dic ={}

for k in n:
    if k not in dic:
        dic[k] =1
    else:
        dic[k] += 1

for k in m:
    if k not in dic:
        print(0, end =" ")
    else:
        print(dic[k], end =" ")
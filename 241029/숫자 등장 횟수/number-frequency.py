d_1= dict()
d_2= dict()

n,m = list(map(int,input().split()))
list_1 = list(map(int,input().split()))
list_2 = list(map(int,input().split()))

for i in range(n):
    if list_1[i] not in d_1:
        d_1[list_1[i]] = 1
    else:
        value = d_1[list_1[i]]
        d_1[list_1[i]] = value+1
for i in range(m):
    if list_2[i] not in d_1:
        print(0, end=" ")
    else:
        print(d_1[list_2[i]], end=" ")
n, m = list(map(int,input().split()))
d_alpa=dict()
d_num=dict()
for i in range(n):
    temp = input()
    value = i +1
    d_alpa[temp] = value
    d_num[value] = temp


for i in range(m):
    temp = input()
    if temp not in d_alpa:
        print(d_num[int(temp)])
    else:
        print(d_alpa[temp])
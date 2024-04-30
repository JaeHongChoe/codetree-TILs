a,bag = map(int,input().split())
money=[]
for k in range(a):
    money.append(list(map(float,input().split())))
    money[k].append(money[k][1]/money[k][0])

money.sort(key = lambda x : -x[2])
ans=0

for k in range(a):
    if bag - money[k][0] <0:
        ans += bag * money[k][2]
        print(f"{ans:.3f}")
        exit()
    bag -= money[k][0]
    ans += money[k][1]
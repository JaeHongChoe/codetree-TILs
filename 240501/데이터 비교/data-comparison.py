a = int(input())
b = list(map(int,input().split()))
b = set(b)

n = int(input())
temp = list(map(int,input().split()))

for k in temp:
    if k in b:
        print(1, end = " ")
    else:
        print(0, end = " ")
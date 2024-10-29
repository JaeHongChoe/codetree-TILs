d=dict()

n = int(input())

for _ in range(n):
    temp = list(map(str,input().split()))
    if temp[0] == "add":
        d[temp[1]] = temp[2]
    elif temp[0] == "remove":
        d.pop(temp[1])
    else:
        if temp[1] not in d:
            print("None")
        else:
            print(d[temp[1]])
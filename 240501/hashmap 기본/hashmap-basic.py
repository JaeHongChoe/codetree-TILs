a = int(input())

b = [
    list(map(str,input().split()))
    for _ in range(a)
]
dic = dict()
for k in b:
    if k[0] in 'add':
        dic[k[1]] = int(k[2])
    elif k[0] in 'find':
        if k[1] not in dic:
            print("None")
        else:
            print(dic[k[1]])
    else:
        if k[1] not in dic:
            print("None")
        else:
            dic.pop(k[1])
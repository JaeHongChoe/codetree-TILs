a, b = map(int,input().split())
li = [
    list(map(int,input().split()))
    for _ in range(b)
]

dic ={}
place =[]

for k in range(a):
    dic[k+1] = [k+1]
    place.append(k+1)

for _ in range(3):
    for k in range(b):
        n = li[k][0]-1
        k = li[k][1]-1
        temp = place[n]
        place[n] = place[k]
        place[k] = temp

        dic[place[n]].append(n+1)
        dic[place[k]].append(k+1)

for ans in dic:
    print(len(set(dic[ans])))
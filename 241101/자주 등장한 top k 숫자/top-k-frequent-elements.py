n,m = list(map(int,input().split()))
lists = list(map(int,input().split()))
d = dict()
many = dict()

for i in range(n):
    if lists[i] not in d:
        d[lists[i]] = 1
    else:
        d[lists[i]] += 1
        
    if d[lists[i]] not in many:
        many[d[lists[i]]] = []
        many[d[lists[i]]].append(lists[i])
    else:
        many[d[lists[i]]].append(lists[i])
    if d[lists[i]] != 1:
        many[d[lists[i]]-1].remove(lists[i])

many_list = sorted(many,reverse=True)
# print(d,lists, many)

ans =[]
for i in many_list:
    # print(sorted(many[i],reverse=True))
    ans.extend(sorted(many[i],reverse=True))
for i in range(m):
    print(ans[i], end = " ")
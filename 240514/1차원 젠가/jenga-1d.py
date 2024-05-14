a = int(input())
block = [ 
    int(input())
    for _ in range(a)
]

for _ in range(2):
    t1, t2 = map(int,input().split())
    temp = block[:t1-1]
    temp.extend(block[t2:])
    block = temp

print(len(block))
for k in block:
    print(k)
n = int(input())
cnt =1
for c in range(n):
    for r in range(n):
        if cnt ==10:
            cnt=1
        print(cnt, end=" ")
        cnt +=1
    print()
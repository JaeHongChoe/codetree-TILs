count = int(input())

for _ in range(count):
    length = int(input())
    lists = list(map(int,input().split()))
    print(lists[0], end = " ")
    for i in range((length//2)+1):
        if i != 0:
            print(sorted(lists[0:(i*2)+1])[(i*2)//2], end = " ")
    print()
count = int(input())

for _ in range(count):
    length = int(input())
    lists = list(map(int,input().split()))
    # arr = []
    # arr.append(lists[0])
    for i in range((length//2)+1):
        # arr.append(lists[(i*2)//2])
        print(lists[(i*2)//2], end = " ")
    print()
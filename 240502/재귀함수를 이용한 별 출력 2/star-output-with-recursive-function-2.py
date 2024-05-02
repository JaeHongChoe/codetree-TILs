a = int(input())


def re(a):
    if a <1 :
        return
    
    for _ in range(a):
        print("*", end = " ")
    print()
    re(a-1)
    for _ in range(a):
        print("*", end = " ")
    print()
re(a)
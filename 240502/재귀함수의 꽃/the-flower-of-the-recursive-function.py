a = int(input())

def re(a):
    if a < 1:
        return
    
    print(a, end =" ")
    re(a-1)
    print(a, end=" ")

re(a)
N, B = map(int, input().split())

def f(n,b):
    if n < 2:
        print(n%b, end="")
        return 0
    f(n//b,b)
    print(n%b, end="")
f(N, B)
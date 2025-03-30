N = int(input())

def f(n):
    if n <=0:
        return 0
    return f(n-2) + n
print(f(N))
# Please write your code here.
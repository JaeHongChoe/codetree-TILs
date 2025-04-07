n = int(input())

def f(n):
    if n <= 0:
        return 0
    f(n//2)
    print(n%2, end="")
f(n)
# Please write your code here.
n = int(input())

def f(n):
    if n == 0:
        return
    f(n-1)
    print("HelloWorld")
f(n)
# Please write your code here.
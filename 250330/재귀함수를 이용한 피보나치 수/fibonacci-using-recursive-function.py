N = int(input())
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    return f(n - 1) +  f(n - 2)
print(f(N))

# Please write your code here.
#An = An-1 + 2 * An-2
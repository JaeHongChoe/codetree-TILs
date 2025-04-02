a, b, c = map(int, input().split())
total = a * b * c

def f(n):
    if n <=0:
        return 0
    return f(n//10) + n%10
    
print(f(total))
# Please write your code here.
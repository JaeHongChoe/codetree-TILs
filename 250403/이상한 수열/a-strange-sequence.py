N = int(input())
# 3 -> 1+2  = 3
# 4 -> 1+3 = 4
# 5 -> 1+4 = 5
# 6 -> 2+5 = 7
# 7 -> 2+7 = 9
# 8 -> 2+9 = 11
# 9 -> 3+11 = 14
# 10 -> 3+14 = 24

def f(n):
    if n ==1:
        return 1
    if n ==2:
        return 2
    return f(n-1)+ f(int(n/3))
print(f(N))
# Please write your code here.
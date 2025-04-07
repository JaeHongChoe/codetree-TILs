N = input()
num = 0

def f(n):
    if n <2:
        print(n%2,end="")
        return 0
    f(n//2)
    print(n%2,end="")
for i in range(len(N)):
    num = num * 2 + int(N[i])
num *= 17
f(num)

# Please write your code here.
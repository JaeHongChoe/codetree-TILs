N = int(input())

def f(n,ans):
    if n == 1:
        print(ans)
        return
    ans +=1
    if n % 2 == 0 :
        f(n/2,ans)
    else:
        f(int(n/3),ans)
f(N,0)

# Please write your code here.
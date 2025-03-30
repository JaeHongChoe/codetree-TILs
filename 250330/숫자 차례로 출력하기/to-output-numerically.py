n = int(input())
cnt = 0
def f(n,cnt):
    if n ==0:
        print()
        return
    cnt +=1
    print(cnt,end=" ")
    f(n-1,cnt)
    print(cnt,end=" ")
f(n,cnt)

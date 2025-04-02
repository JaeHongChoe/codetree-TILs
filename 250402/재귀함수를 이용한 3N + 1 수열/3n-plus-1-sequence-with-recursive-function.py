n = int(input())
cnt=0
def f(n,cnt):
    if n == 1:
        return cnt
    cnt +=1
    if n % 2 ==0:
        return f(n/ 2,cnt) 
    else:
        return f(n* 3 + 1,cnt)
print(f(n,cnt))
# Please write your code here.
a, b = map(int, input().split())
ans =0

def f(k):
    if k % 2 ==0:
        return 0
    if k % 10  == 5:
        return 0
    if k % 3 == 0 and k % 9 !=0:
        return 0
    return k

while a != b+1 :
    temp = f(a)
    if temp !=0:
        ans +=1
    a +=1
print(ans)
# Please write your code here.
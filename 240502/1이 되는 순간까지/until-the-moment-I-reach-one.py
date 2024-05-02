a = int(input())

cnt=0
def re(a,cnt):
    if a <=1:
        print(cnt)
        return 
    if a %2 ==0:
        cnt+=1
        re(a/2,cnt)
    else:
        cnt+=1
        re(a//3,cnt)

re(a,cnt)
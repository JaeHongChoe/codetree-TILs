n= list(map(int,input().split()))

def test(n):
    ans =0
    if len(n) <2:
        return ans

    for k in range(n[0],n[1]+1):
        if k %2 !=0 and k %3 !=0:
            ans+=k
    return ans 

print(test(n))
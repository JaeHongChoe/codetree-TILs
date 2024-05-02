a = int(input())
ans=0
def fact(a,ans):
    if a <1:
        return ans
    ans += a
    return fact(a-1,ans)

print(fact(a,ans))
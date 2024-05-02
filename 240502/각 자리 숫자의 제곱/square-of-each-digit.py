a = int(input())

def re(a):
    if a <10:
        return a**2
    # print(a%10)
    return re(a//10) + (a%10)**2

print(re(a))
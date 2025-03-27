M, D = map(int, input().split())

more = [1,3,5,7,8,10,12]
less = [4,6,9,11]

def f(m,d):
    if m == 2 and d < 29:
        return "Yes"
    elif m == 2 and d > 29:
        return "No"
    
    if m in more and d < 32:
        return "Yes"
    elif m in more and d > 32:
        return "No"
    
    if m in less and d < 31:
        return "Yes"
    elif m in less and d > 31:
        return "No"
    
    return "No"

print(f(M,D))
# Please write your code here.
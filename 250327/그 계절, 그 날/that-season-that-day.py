Y, M, D = map(int, input().split())

more = [1,3,5,7,8,10,12]
less = [4,6,9,11]

def season(m):
    if m >= 3 and m <= 5:
        return "Spring"
    elif m >= 6 and m <= 8:
        return "Summer"
    elif m >= 9 and m <= 11:
        return "Fall"
    else:
        return "Winter"

def f(y,m,d):
    
    if m in more and d < 32:
        return season(m)
    elif m in more and d > 32:
        return -1
    
    if m in less and d < 31:
        return season(m)
    elif m in less and d > 31:
        return -1

    yoon = 0
    if m == 2:
        if y % 4 == 0:
            yoon = 1
            if y % 100 == 0 and y % 400 != 0:
                yoon = 0

    if m == 2 and d < 30 and yoon == 1:
        return season(m)
    elif m == 2 and d < 29 and yoon == 0:
        return season(m)
    else:
        return -1

print(f(Y,M,D))
# Please write your code here.
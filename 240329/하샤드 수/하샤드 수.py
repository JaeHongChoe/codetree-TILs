def solution(x):
    x_s=0
    x_s = sum([int(a) for a in str(x)])
    if x % x_s ==0:
        return True
    return False

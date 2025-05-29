m = int(input())
a, b = map(int, input().split())

ans_min = 999999999
ans_max = 0

def check(target):
    left, right = 1, m
    cnt = 0
    while left <=right:
        mid = (left+right)//2
        cnt +=1
        if mid < target:
            left = mid +1
        elif mid > target:
            right = mid-1
        else:
            return cnt
    return cnt

for i in range(a,b+1):
    count = check(i)
    if ans_max < count:
        ans_max = count
    if ans_min > count:
        ans_min = count
print(ans_min,ans_max)

# Please write your code here.

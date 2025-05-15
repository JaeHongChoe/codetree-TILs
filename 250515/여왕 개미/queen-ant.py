# 7
# 100 5 2 4 7 8 15
# 400 1
# 400 2
# 200 50
# 400 2
# 300 5
# 400 
# 2, 3, 1, 35]
#2, 3, 1, 35,1]
# [2, 3, 1, 90 1,2,35]
k = int(input())
build = list(map(int,input().split()))
house = sorted(build[2:])

def search(ants, house):
    left = 0
    right = house[-1] - house[0]
    answer = right

    while left <= right:
        mid = (left + right) // 2

        # print(left,right, mid)
        count = 1
        start = house[0]
        for h in house[1:]:
            if h - start > mid:
                count += 1
                start = h
        if count <= ants:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
   


for i in range(k-1):
    order, task = map(int,input().split())
    if order == 400:
        # print(house)
        print(search(task,house))
    elif order == 200:
        house.append(task)
    else:
        del house[task-1]




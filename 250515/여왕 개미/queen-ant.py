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
house = build[2:]

def search(ants,house):
    time = 0
    if ants == 1:
        return house[-1] - house[0]
    else:
        temp = []
        for i in range(len(house)-1):
            temp.append(house[i+1]-house[i])
        # print(temp)
        for i in range(ants-1):
            loc = temp.index(max(temp))
            temp[loc] = 0
        # print(temp)
        total = 0
        for i in temp:
            if i != 0:
                total += i
            else:
                if time <total:
                    time = total
                total = 0
        return time


    return 0

for i in range(k-1):
    order, task = map(int,input().split())
    if order == 400:
        print(search(task,house))
    elif order == 200:
        house.append(task)
    else:
        del house[task-1]
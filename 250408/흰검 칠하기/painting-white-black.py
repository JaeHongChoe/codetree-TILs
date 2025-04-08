n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
line = {}
status_1 = 0
status_2 = 0
for num, direction in commands:
    if direction == "R" and int(num) != 1:
        status_1 += int(num)-1
        for i in range(status_2, status_1+1):
            if i in line:
                line[i][0] += 1
                line[i][1] = "B"
            else:
                line[i] = [1,"B"]
    elif direction == "R" and int(num) == 1:
        if status_1 in line:
            line[status_1][0] += 1
            line[status_1][1] = "B"
        else:
            line[status_1] = [1,"B"]
    elif direction == "L" and int(num) == 1:
        if status_1 in line:
            line[status_1][0] += 1
            line[status_1][1] = "W"
        else:
            line[status_1] = [1,"W"]
    else:
        status_1 -= int(num)-1
        for i in range(status_1, status_2+1 , 1):
            if i in line:
                line[i][0] += 1
                line[i][1] = "W"
            else:
                line[i] = [1,"W"]
    status_2 = status_1

w , b, g = 0,0,0

for i, k in line.values():
    if i >=4:
        g+=1
    elif k == "W":
        w +=1
    elif k == "B":
        b +=1
print(w,b,g)
# Please write your code here.
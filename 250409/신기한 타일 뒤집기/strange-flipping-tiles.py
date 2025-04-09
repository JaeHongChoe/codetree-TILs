n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
line = {}
status = 0
for num, direction in commands:
    if direction == 'R':
        for i in range(int(num)):
            line[status+i] = "R"
        status += int(num) -1
    else:
        for i in range(int(num)):
            line[status-i] = "L"
        status -= int(num) -1
print(list(line.values()).count("L"),list(line.values()).count("R"))
# Please write your code here.
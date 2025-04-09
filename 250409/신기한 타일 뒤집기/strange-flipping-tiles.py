n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
line = {}
for num, direction in commands:
    for i in range(int(num)):
        if direction == 'R':
            line[i] = "R"
        else:
            line[i] = "L"
print(list(line.values()).count("L"),list(line.values()).count("R"))
# Please write your code here.
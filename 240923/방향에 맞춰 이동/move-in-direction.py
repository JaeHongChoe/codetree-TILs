a = int(input())
grid = [
    list(map(str,input().split()))
    for _ in range(a)
]
x,y =0,0
#서남동북
b = [(0,-1),(-1,0),(0,1),(1,0)]
for i in range(a):
    if grid[i][0] == "N":
        for _ in range(int(grid[i][1])):
            x+=b[3][1]
            y+=b[3][0]
    elif grid[i][0] =="E":
        for _ in range(int(grid[i][1])):
            x+=b[2][1]
            y+=b[2][0]
    elif grid[i][0] =="S":
        for _ in range(int(grid[i][1])):
            x+=b[1][1]
            y+=b[1][0]
    elif grid[i][0] =="W":
        for _ in range(int(grid[i][1])):
            x+=b[0][1]
            y+=b[0][0]
print(x,y)
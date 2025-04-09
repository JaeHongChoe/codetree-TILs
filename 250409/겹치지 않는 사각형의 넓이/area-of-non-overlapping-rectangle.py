x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3
offset = 1000
ans = 0
x1[0], y1[0], x2[0], y2[0] = map(int, input().split()) 
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

grid = [[0]*2000 for _ in range(2000)]
for k in range(3):
    off_x1, off_x2, off_y1, off_y2 = x1[k]+offset,x2[k]+offset,y1[k]+offset,y2[k]+offset
    for i in range(off_y1,off_y2):
        for j in range(off_x1,off_x2):
            if k != 2 and grid[i][j] == 0:
                grid[i][j] = 1
                ans +=1
            elif k ==2 and grid[i][j] == 1:
                grid[i][j] = 0
                ans -=1
print(ans)
# Please write your code here.
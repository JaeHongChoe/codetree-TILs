board = [list(map(int, input().split())) for _ in range(19)]
ans = 0
def in_range(x, y):
    return 0 <= x and x < 19 and 0 <= y and y < 19
    
# (x, y)에서 시작하여 next_dir 방향으로
# 이동한 이후의 위치를 반환합니다.
# down : 1,0
# right : 0,1
# down_left : 1,-1
# down_right : 1,1
def check(x, y,dirr,flag):
    dxs, dys = [1, 0, 1, 1], [0, 1, -1, 1]
    nx, ny = x + dxs[dirr], y + dys[dirr]
    if flag >= 5:
        print(board[x][y])
        print(1 + nx - dxs[dirr]*3 ,1 + ny - dys[dirr]*3)
        return 1
    else:
        if in_range(nx,ny) and board[nx][ny] == board[x][y]:
            flag +=1
            return check(nx,ny,dirr,flag)

for i in range(19):
    for k in range(19):
        if board[i][k] != 0 and ans == 0:
            for j in range(4):
                flag = 1
                if check(i,k,j,flag):
                    ans = 1
if ans == 0:
    print(0)

# Please write your code here.
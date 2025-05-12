board = [list(map(int, input().split())) for _ in range(19)]

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
    if in_range(nx,ny) and board[nx][ny] == board[x][y]:
        flag +=1
        if flag >= 5:
            print(board[x][y])
            print(1 + nx - dxs[dirr]*2 ,1 + ny - dys[dirr]*2)
            return ""
        else:
            check(nx,ny,dirr,flag)

for i in range(19):
    for k in range(19):
        if board[i][k] != 0:
            for j in range(4):
                flag = 1
                check(i,k,j,flag)

# Please write your code here.
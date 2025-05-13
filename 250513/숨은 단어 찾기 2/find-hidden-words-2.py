N, M = map(int, input().split())
arr = [input() for _ in range(N)]
ans =0

def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < M
    
# (x, y)에서 시작하여 next_dir 방향으로
# 이동한 이후의 위치를 반환합니다.
# up : -1, 0
# up_right : -1, 1
# right : 0,1
# down_right : 1,1
# down : 1,0
# down_left : 1,-1
# left : 0, -1
# up_left : -1, -1

def check(x, y,dirr,flag):
    dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    nx, ny = x + dxs[dirr], y + dys[dirr]
    if flag >= 2:
        return 1
    elif in_range(nx,ny) and arr[nx][ny] == "E":
        flag +=1
        return check(nx,ny,dirr,flag)
    else:
        return 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == "L":
            for dirr in range(8):
                flag = 0
                ans += check(i,j,dirr,flag)
print(ans)
# Please write your code here.
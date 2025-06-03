n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

def in_range(y,x):
    return x >= 0 and x <= n-1 and y >= 0 and y <= n-1  
def tornado():
    global arr
    ans = 0
    x, y = n//2, n//2
    d = [(0,-1),(1,0),(0,1),(-1,0)]

    clean_borad = [    (-2,0),
                (-1,-1),(-1,0),(-1,1),
        (0,-2),(0,-1),          (0,1),(0,2),
                (1,-1), (1,0), (1,1),
                        (2,0)]
    clean_d = [(5,2,9,1,12,3,10,4,11,6),
                (12,9,11,5,8,6,7,2,4,10),
                (8,4,11,1,12,3,10,2,9,7),
                (1,2,4,5,8,6,7,9,11,3)]
    
    d_idx = 0
    dist = 1
    move_count = 0
    while True:
        for _ in range(dist):
            ry, rx = d[d_idx]
            y += ry
            x += rx
            rd = clean_d[d_idx]
            if (y,x) == (0,-1):
                return ans
            curr = arr[y][x]
            temp = 0
            for i in range(10):
                if i == 0:
                    curr_dust = int(curr *0.05)
                elif i in [1,2]:
                    curr_dust = int(curr *0.1)
                elif i in [3,4]:
                    curr_dust = int(curr *0.02)
                elif i in [5,6]:
                    curr_dust = int(curr *0.07)
                elif i in [7,8]:
                    curr_dust = int(curr *0.01)
                else:
                    curr_dust = curr-temp
                temp += curr_dust
                oy, ox = y+clean_borad[rd[i]-1][0], x+clean_borad[rd[i]-1][1]
                if not in_range(oy,ox):
                    ans += curr_dust
                    continue
                arr[oy][ox] += curr_dust
            arr[y][x] = 0
        move_count += 1
        d_idx = (d_idx+1)%4
        if move_count == 2:
            move_count = 0
            dist +=1
print(tornado())

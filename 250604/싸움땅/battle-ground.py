n, m, k = map(int,input().split())
temp = [list(map(int,input().split())) for _ in range(n)]
player = [list(map(int,input().split())) +[0] for _ in range(m)] #x,y,d,s
arr = [[[nn] for nn in row] for row in temp]
score = [0]*m
visited = [[0]*n for _ in range(n)]
for i in range(m):
    visited[player[i][0]-1][player[i][1]-1] = i+1

def in_range(y,x):
    return x >= 0 and x <= n-1 and y >= 0 and y <= n-1

def sim():
    global arr, player,socre
    d = [(-1,0),(0,1),(1,0),(0,-1)]
    for i in range(m):
        ry, rx = player[i][0]-1, player[i][1]-1
        oy, ox = ry + d[player[i][2]][0], rx + d[player[i][2]][1]
        if not in_range(oy,ox):
            idx = (player[i][2] + 2)%4
            oy, ox = ry + d[idx][0], rx +d[idx][1]
            player[i][2] = idx
        if visited[oy][ox] != 0:
            # print(i+1)
            # fight
            someone = visited[oy][ox] -1
            someone_power = player[someone][3] + player[someone][4]
            player_power = player[i][3] + player[i][4]
            if someone_power == player_power:
                someone_power = player[someone][3]
                player_power = player[i][3]
            # print(someone, someone_power, player_power)
            if someone_power > player_power:
                score[someone] += (player[someone][3] + player[someone][4]) - (player[i][3] + player[i][4]) 
                visited[player[i][0]-1][player[i][1]-1] = 0
                ry, rx = oy, ox
                oy, ox = ry + d[player[i][2]][0], rx + d[player[i][2]][1]
                idx = player[i][2] 
                while (not in_range(oy,ox)) or visited[oy][ox] != 0:
                    idx = (idx + 1)%4
                    player[i][2] = idx
                    oy, ox = ry + d[idx][0], rx +d[idx][1]
                if player[i][4] !=0:
                    arr[ry][rx].append(player[i][4])
                    arr[ry][rx] = sorted(arr[ry][rx],reverse=True)
                    player[i][4] = 0
                visited[oy][ox] = i+1
                player[i][0], player[i][1] = oy+1, ox+1
                player[i][4] = arr[oy][ox][0]
                arr[oy][ox][0] = 0
                arr[oy][ox] = sorted(arr[oy][ox],reverse=True)
            elif someone_power < player_power:
                score[i] += (player[i][3] + player[i][4]) - (player[someone][3] + player[someone][4])
                visited[player[i][0]-1][player[i][1]-1] = 0
                ry, rx = oy, ox
                oy, ox = ry + d[player[someone][2]][0], rx + d[player[someone][2]][1]
                idx = player[someone][2]
                while (not in_range(oy,ox)) or visited[oy][ox] != 0:
                    idx = (idx + 1)%4
                    player[someone][2] = idx
                    oy, ox = ry + d[idx][0], rx +d[idx][1]
                if player[someone][4] !=0:
                    arr[ry][rx].append(player[someone][4])
                    arr[ry][rx] = sorted(arr[ry][rx],reverse=True)
                    player[someone][4] = 0
                if player[i][4] !=0:
                    arr[ry][rx].append(player[i][4])
                    arr[ry][rx] = sorted(arr[ry][rx],reverse=True)
                    player[i][4] = 0
                visited[ry][rx] = i+1
                player[i][4] = arr[ry][rx][0]
                arr[ry][rx][0] = 0
                arr[ry][rx] = sorted(arr[ry][rx],reverse=True)

                visited[oy][ox] = someone+1
                player[i][0], player[i][1] = ry+1, rx+1
                player[someone][0], player[someone][1] = oy+1, ox+1
                player[someone][4] = arr[oy][ox][0]
                arr[oy][ox][0] = 0
                arr[oy][ox] = sorted(arr[oy][ox],reverse=True) 
        else:
            visited[player[i][0]-1][player[i][1]-1] = 0
            visited[oy][ox] = i+1
            player[i][0], player[i][1] = oy+1, ox+1
            if player[i][4] !=0:
                arr[oy][ox].append(player[i][4])
                arr[oy][ox] = sorted(arr[oy][ox],reverse=True)
                player[i][4] = 0
            player[i][4] = arr[oy][ox][0]
            arr[oy][ox][0] = 0
            arr[oy][ox] = sorted(arr[oy][ox],reverse=True)








for _ in range(k):
    sim()
for i in score:
    print(i, end=" ")
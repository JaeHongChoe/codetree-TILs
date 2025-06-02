n = int(input())
arr = [list(map(int,input().split())) for _ in range(n*n)]

def in_range(x,y):
    return 0 <= x and x <= n-1 and y >= 0 and y <= n-1

def find_friends(arr,i):
    d = [(0,1), (1,0), (0,-1), (-1,0)]
    place = [[0]*n for _ in range(n)]
    max_num = 0
    for j in range(n):
        for k in range(n):
            if arr[j][k] in i[1:]:
                for d_idx in range(4):
                    dy, dx = d[d_idx]
                    if in_range(k+dx,j+dy) and arr[j+dy][k+dx] == 0:
                        place[j+dy][k+dx] += 1
                        max_num = max(max_num, place[j+dy][k+dx])
    return place, max_num

def loca(place,max_num,arr):
    d = [(0,1), (1,0), (0,-1), (-1,0)]
    place_empty = [[0]*n for _ in range(n)]
    empty_max = 0
    place_to_put = []
    for i in range(n):
        for k in range(n):
            if place[i][k] == max_num and arr[i][k] == 0:
                place_empty[i][k] += 1
                for d_idx in range(4):
                    dy, dx = d[d_idx]
                    if in_range(k+dx,i+dy) and place[i+dy][k+dx] == 0 and arr[i+dy][k+dx] ==0:
                        place_empty[i][k] += 1
                if place_empty[i][k] > empty_max:
                    place_to_put = []
                    empty_max = place_empty[i][k]
                    place_to_put.append([i,k])
                elif place_empty[i][k] == empty_max:
                    place_to_put.append([i,k])
    # print(place_empty,place_to_put)
    if len(place_to_put) > 1:
        ans = []
        place_to_put = sorted(place_to_put)
        min_x = place_to_put[0][0]
        ans.append(place_to_put[0])
        for i in range(len(place_to_put)):
            if place_to_put[i][0] == min_x:
                ans.append(place_to_put[i])
        ans = sorted(ans)
        return ans[0]
    elif len(place_to_put) == 1:
        return place_to_put[0]



def sim(arr):
    new_arr = [[0]*n for _ in range(n)]
    for i in arr:
        place,max_num = find_friends(new_arr,i)
        place_empty = loca(place,max_num,new_arr)
        new_arr[place_empty[0]][place_empty[1]] = i[0]
    ans = 0
    for i in range(n):
        d = [(0,1), (1,0), (0,-1), (-1,0)]
        for k in range(n):
            for j in arr:
                if j[0] == new_arr[i][k]:
                    cnt = 0
                    for d_idx in range(4):
                        dy, dx = d[d_idx]
                        if in_range(k+dx,i+dy) and new_arr[i+dy][k+dx] in j[1:]:
                            cnt +=1
                    ans += (10**cnt)//10
    return ans

print(sim(arr))
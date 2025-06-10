import sys
sys.stdin = open("./input.txt")
input = sys.stdin.readline
from collections import deque
n, p = map(int,input().split())
p_arr = [list(map(int,input().split())) for _ in range(p)]
arr=[[0]*n for _ in range(n)]

def put_arr():
    for i in range(p_arr[ii][1],p_arr[ii][3]):
        for k in range(p_arr[ii][0], p_arr[ii][2]):
            arr[i][k] = ii+1
def in_range(y,x):
    return x>=0 and x<n and y>=0 and y<n
def search_die():
    d = [(0,-1),(1,0),(0,1),(-1,0)]
    check = [0]*p
    visited = [[0] * n for _ in range(n)]
    v = [[] for _ in range(p)]
    for i in range(n):
        for k in range(n):
            if arr[i][k] !=0 and visited[i][k]==0:
                visited[i][k]=1
                q = deque()
                q.append((i,k))
                type = arr[i][k]
                check[type-1] +=1
                v[type - 1].append([i, k])
                while q:
                    y,x = q.popleft()
                    for loc in range(len(d)):
                        dy, dx = d[loc]
                        oy, ox = dy+y,dx+x
                        if in_range(oy,ox) and visited[oy][ox]==0 and arr[oy][ox]==type:
                            visited[oy][ox]=1
                            q.append((oy,ox))
                            v[type-1].append([oy,ox])
    many = [0]*p
    for i in range(p):
        if check[i] >=2:
            for ll in v[i]:
                arr[ll[0]][ll[1]]=0
            v[i]=[]
        many[i]=(len(v[i]),i*-1)
    return sorted(many,reverse=True),v,many

def put_new(service, ser_list):
    new_arr = [[0] * n for _ in range(n)]
    for i in service:
        if i[0] == 0:
            continue
        _,idx = i
        idx*=-1
        min_y=(99999,99999)
        min_x=(99999,99999)
        for k in range(len(ser_list[idx])):
            y,x = ser_list[idx][k]
            if min_x > (x,y):
                min_x=(x,y)
            if min_y>(y,x):
                min_y=(y,x)
        init_y =  min_y[0]
        init_x =  min_x[0]
        for k in range(len(ser_list[idx])):
            ser_list[idx][k] = [ser_list[idx][k][0]-init_y,ser_list[idx][k][1]-init_x]

        x_idx=0
        y_idx=0
        flag=True
        while flag:
            cnt=0
            for k in range(len(ser_list[idx])):
                y,x = ser_list[idx][k]
                oy, ox = y+y_idx,x+x_idx
                if not in_range(oy, ox):
                    if oy >=n:
                        y_idx=0
                        x_idx+=1
                        break
                    if ox >=n:
                        flag=False
                        break
                if new_arr[oy][ox] !=0:
                    y_idx+=1
                    break
                cnt+=1
                if flag==True and cnt == len(ser_list[idx]):
                    for k in range(len(ser_list[idx])):
                        y, x = ser_list[idx][k]
                        oy, ox = y+y_idx, x+x_idx
                        new_arr[oy][ox] = idx+1
                    flag=False
    return new_arr

def search_many():
    d = [(0,-1),(1,0),(0,1),(-1,0)]
    v = []
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if arr[i][k] !=0 and visited[i][k]==0:
                visited[i][k]=1
                q = deque()
                q.append((i,k))
                type = arr[i][k]
                while q:
                    y,x = q.popleft()
                    for loc in range(len(d)):
                        dy, dx = d[loc]
                        oy, ox = dy+y,dx+x
                        if in_range(oy,ox) and visited[oy][ox]==0 and arr[oy][ox]==type:
                            visited[oy][ox]=1
                            q.append((oy,ox))
                        elif in_range(oy,ox)  and (arr[oy][ox]!=type and arr[oy][ox]!=0):
                            temppp = sorted((type,arr[oy][ox]))
                            if temppp not in v:
                                v.append(temppp)

    return v

for ii in range(p):
    put_arr()
    # print("first")
    # for i in range(n):
    #     print(arr[i])
    # print()
    service, ser_list,for_score= search_die()
    new_arr = put_new(service, ser_list)
    arr=new_arr
    test = search_many()
    temp = 0
    if len(test)==0:
        print(0)
    else:
        for i in range(len(test)):

            t1,t2 = test[i]
            t1-=1
            t2-=1
            val1,_ = for_score[t1]
            val2,_ = for_score[t2]
            temp+=val1*val2
        print(temp)
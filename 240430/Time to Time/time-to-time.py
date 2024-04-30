a = list(map(int,input().split()))

own = (a[2] - a[0]-1)*60

left_time = 60 - a[1]


print(own + left_time + a[3])
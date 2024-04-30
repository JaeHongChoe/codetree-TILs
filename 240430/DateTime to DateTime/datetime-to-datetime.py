a = list(map(int,input().split()))
left_date = a[0] -11

total = -11 - 11*60
total += a[2] + a[1]*60 + left_date *1440

print(total)

# 11/11월 12일13시14분
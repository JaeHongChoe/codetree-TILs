n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0
while(0 != len(coins)):
    if k - coins[-1] <0:
        del coins[-1]
    else:
        k -= coins[-1]
        cnt +=1
print(cnt)
# Please write your code here.

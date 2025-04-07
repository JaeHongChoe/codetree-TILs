n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
cnt=0
str = sorted(str)
for i in str:
    if i[:len(t)] == t:
        cnt +=1
    if cnt == k:
        print(i)
        break
# print(str)
# Please write your code here.
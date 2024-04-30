a,b = map(int,input().split())
money = [
    int(input())
    for _ in range(a)
]
cnt=0
place=1
while(b !=0):
    if b - money[place*-1] >=0:
        b -= money[place*-1]
        cnt +=1
        
    else:
        place+=1
    

print(cnt)
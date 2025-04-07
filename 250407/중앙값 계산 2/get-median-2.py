n = int(input())
arr = list(map(int, input().split()))

for i in range(0,n,2):
    temp = sorted(arr[:i+1])
    print(temp[i//2],end=" ")

# Please write your code here.
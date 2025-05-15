n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

def check():
    for k in range(n):
        if queries[i] == arr[k]:
            return k+1
    return -1

for i in range(m):
    print(check())


# Please write your code here.

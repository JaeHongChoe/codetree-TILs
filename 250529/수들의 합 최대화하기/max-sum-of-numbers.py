n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [0] *n
arr = [i for i in range(n)]
ans = 0
def choose(num, new_arr):
    global grid, arr, ans
    if len(new_arr) == num:
        temp = 0
        for i in range(num):
            temp += grid[i][new_arr[i]]
        ans = max(ans, temp)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            choose(num, new_arr+[arr[i]])
            visited[i] = 0

choose(n,[])
print(ans)


# Please write your code here.

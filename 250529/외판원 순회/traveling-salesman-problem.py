n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
visited = [0]*n
arr = [i for i in range(n)]
ans = 99999999

def check(check_arr):
    if abs(check_arr[0]-check_arr[-1]) != 1 or abs(check_arr[0] - check_arr[-1]) == n-1:
        return False
    return True

def chosoe(num, new_arr):
    global arr, ans, A
    if len(new_arr) == num and check(new_arr):
        temp = 0
        for k in range(num):
            if A[k][new_arr[k]] == 0:
                return
            temp += A[k][new_arr[k]]
        ans = min(ans, temp)
        return
    for i in range(num):
        if not visited[i]:
            visited[i] = 1
            chosoe(num,new_arr+[arr[i]])
            visited[i] = 0

chosoe(n,[])
print(ans)
# Please write your code here.

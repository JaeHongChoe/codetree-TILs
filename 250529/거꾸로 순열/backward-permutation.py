n = int(input())
visited = [0]*n
arr = [i+1 for i in range(n)]

def choose(num, new_arr):
    global arr
    if len(new_arr) == num:
        for k in new_arr:
            print(k,end=" ")
        print()
        return
    for i in range(n-1,-1,-1):
        if not visited[i]:
            visited[i] = 1
            choose(num,new_arr+[arr[i]])
            visited[i] = 0

choose(n,[])
# Please write your code here.

n = int(input())
arr = [i for i in range(1,n+1)]
visited = [0] * n

def choose(num,new_arr):
    global arr
    if len(new_arr) == n:
        for k in new_arr:
            print(k,end = " ")
        print()
        return
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = 1
            choose(num,new_arr+[arr[i]])
            visited[i] = 0
choose(n,[])
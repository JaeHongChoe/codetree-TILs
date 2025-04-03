n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

def f(n,A,B):
    for i in range(n):
        if A[i] - B[i] !=0:
            return "No"
    return "Yes"
print(f(n,A,B))
# Please write your code here.
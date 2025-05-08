R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]
ans = 0
start = grid[0][0]
for i in range(1,R):
    for k in range(1,C):
        if grid[i][k] != start:
            for one_i in range(i+1,R):
                for one_k in range(k+1,C):
                    if grid[one_i][one_k] == start:
                        for two_i in range(one_i+1,R):
                            for two_k in range(one_k+1,C):
                                if grid[two_i][two_k] != start and two_i+1 == R and two_k+1 == C:
                                    ans+=1
print(ans)

# Please write your code here.
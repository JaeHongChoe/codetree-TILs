n = int(input())

stack =[]
matrix = [list(map(str, input().split())) for _ in range(n)]

# print(matrix)
for k in matrix:
    if k[0] in ['push_back']:
        stack.append(int(k[1]))
    elif(k[0] in ['pop_back']):
        del stack[-1]
    elif(k[0] in ['size']):
        print(len(stack))
    else:
        print(stack[int(k[1])-1])

    # print(o)


# print(n)
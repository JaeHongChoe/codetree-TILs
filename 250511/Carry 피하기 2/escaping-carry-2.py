n = int(input())
arr = [int(input()) for _ in range(n)]
ans = -1


for i in range(n-2):
    for k in range(i+1,n-1):
        for j in range(k+1,n):
            total = len(str(max(arr[i] , arr[k] , arr[j])))
            temp1 = arr[i]
            temp2 = arr[k]
            temp3 = arr[j]
            for m in range(total):
                flag = 1
                if 9 < (temp1 % 10 + temp2 % 10 + temp3 % 10):
                    flag = -1
                    break
                temp1 = temp1// 10
                temp2 = temp2// 10
                temp3 = temp3// 10

            if ans < (arr[i] + arr[k] + arr[j]) * flag:
                ans = arr[i] + arr[k] + arr[j]

print(ans)

            # temp = arr[i] + arr[k] + arr[j]



# Please write your code here.
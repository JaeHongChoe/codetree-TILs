s = int(input())
ans = 0
left , right = 1, s//2
while left <= right:
    mid = (left+right)//2
    if mid *(mid+1)//2 <=s:
        ans = max(ans,mid)
        left = mid +1
    else:
        right = mid -1
print(ans)

# Please write your code here.

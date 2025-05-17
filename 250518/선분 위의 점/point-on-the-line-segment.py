n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]
points = sorted(points)

def check(target):
    left, right = 0, n-1
    idx = n
    while left <= right:
        mid = (left + right) // 2
        if points[mid] < target:
            left = mid +1
        else:
            idx = min(idx,mid)
            right = mid - 1
    return idx
for seg_left,seg_right in segments:
    a = check(seg_right)
    b = check(seg_left)
    ans = a-b
    if a < n and points[a] == seg_right:
        ans +=1
    print(ans)

# Please write your code here.

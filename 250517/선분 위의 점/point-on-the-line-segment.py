n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]
points = sorted(points)
for seg_left,seg_right in segments:
    ans = 0
    for k in points:
        if k >= seg_left and k <= seg_right:
            left, right = seg_left, seg_right
            while left <= right:
                mid = (left + right) // 2
                if mid < k:
                    left = mid +1
                elif mid > k:
                    right = mid - 1
                else:
                    ans += 1
                    break
    print(ans)

# Please write your code here.

def solution(s):
    ans = 0
    s = s.split()
    for i in range(len(s)):
        if s[i] not in 'Z':
            ans += int(s[i])
        else:
            ans -= int(s[i-1])
    return ans

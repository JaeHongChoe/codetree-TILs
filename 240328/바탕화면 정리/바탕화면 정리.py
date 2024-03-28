def solution(wallpaper):
    answer = [0 for i in range(4)]
    answer[0] = 999
    answer[1] = 999
    
    for i_i,i in enumerate(wallpaper):
        for k_i,k in enumerate(i):
            if k == '#':
                answer[0] = min(int(i_i),answer[0])
                answer[1] = min(int(k_i),answer[1])
                answer[2] = max(int(i_i)+1,answer[2])
                answer[3] = max(int(k_i)+1,answer[3])
    
    return answer


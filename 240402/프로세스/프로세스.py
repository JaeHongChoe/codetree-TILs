def solution(priorities, location):
    answer = 0
    cnt=0
    place = [0 for i in range(len(priorities))]
    place[location] = 1
    
    while(True):
        sort =[]
        kk =[]
        m_i = priorities.index(max(priorities))
        
        cnt+=1
        sort.extend(priorities[m_i:])
        kk.extend(place[m_i:])
        
        sort.extend(priorities[:m_i])
        kk.extend(place[:m_i])

        priorities = sort
        place = kk
        
        sort[0]=0
        
        if place[0] ==1 and cnt ==1:
            return cnt
        elif place[0] ==1 and cnt >1:
            return cnt
        

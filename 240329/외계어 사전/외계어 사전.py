def solution(spell, dic):
    
    for i in dic:
        if len(spell) == len(i):
            temp = spell.copy()
            ans =0
            for k in i:
                if k in temp:
                    temp[temp.index(k)] = 0
                    ans+=1
                else:
                    continue
            if ans == len(spell):
                return 1
    return 2

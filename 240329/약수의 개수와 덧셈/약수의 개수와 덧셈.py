def solution(left, right):
    answer = [0 for _ in range(right-left+1)]
    cnt=0
    for i in range(left,right+1,1):
        temp =[]
        for k in range(1,i+1,1):
            if i % k ==0:
                temp.append(k)
                
        if len(temp) %2==0:
            answer[cnt] = temp[-1]
        else:
            answer[cnt] = temp[-1]*-1
        cnt +=1
                
    return sum(answer)

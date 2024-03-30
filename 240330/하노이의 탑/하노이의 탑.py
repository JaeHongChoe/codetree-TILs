def solution(n):
    ans=[]
    def hnoi(n, start, end,temp):
        
        if n ==1:
            ans.append([start,end])
            return ans
        
        hnoi(n-1, start, temp,end)
        ans.append([start,end])
        hnoi(n-1, temp, end,start)
        
    hnoi(n,1,3,2)
    return ans

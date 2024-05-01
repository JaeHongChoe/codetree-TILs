from collections import deque

a, b = map(int,input().split())
cnt=1
dq = deque()
dq_temp = deque()
ans =[]

for x in range(1,a+1):
    dq.append(x)

while(dq):
    while(dq):
        if cnt == b:
            # ans.append(dq.popleft())
            print(dq.popleft(), end=" ")
            cnt =1
        else:
            dq_temp.append(dq.popleft())
            cnt+=1
    
    dq = dq_temp
    dq_temp = deque()
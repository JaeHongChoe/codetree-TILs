preorder = list() 
postorder = list()
def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(10**6)
    levels = sorted(list({x[1] for x in nodeinfo}),reverse=True) # 유효한 Y좌표
    nodes = sorted(list(zip(range(1,len(nodeinfo)+1),nodeinfo)),key=lambda x:(-x[1][1],x[1][0])) # 노드 정렬
    order(nodes,levels,0)
    return [preorder,postorder]

def order(nodes,levels,curlevel):
    n = nodes[:] # copy
    cur = n.pop(0) # VISIT
    preorder.append(cur[0]) # PRE-ORDER
    if n: # stop if leaf node
        for i in range(len(n)): # find next floor
            if n[i][1][1] == levels[curlevel+1]: # next floor
                if n[i][1][0] < cur[1][0]: # LEFT CHILD
                    order([x for x in n if x[1][0] < cur[1][0]],levels,curlevel+1)
                else: # RIGHT CHILD
                    order([x for x in n if x[1][0] > cur[1][0]],levels,curlevel+1)
                    break
    postorder.append(cur[0]) # POST-ORDER

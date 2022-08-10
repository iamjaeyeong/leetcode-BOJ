import math

def solution(k, num, links):
    answer = 0
    inf = math.inf

    def count(limit, links, partial_sum, nodes, max_depth, ret=[0]):
        for depth in range(max_depth, -1, -1):
            for node in nodes[depth]:
                if links[node][0]!=-1:
                    partial_sum[node] += partial_sum[links[node][0]]
                if links[node][1]!=-1:
                    partial_sum[node] += partial_sum[links[node][1]]
                    
                if partial_sum[node]>limit:
                    if links[node]==[-1, -1]:
                        ret[0] += inf
                        return
                    elif links[node][0]==-1:
                        partial_sum[node] -= partial_sum[links[node][1]]
                        if partial_sum[links[node][1]] > limit:
                            ret[0] += inf
                            return
                        else:
                            ret[0] += 1
                    elif links[node][1]==-1:
                        partial_sum[node] -= partial_sum[links[node][0]]
                        if partial_sum[links[node][0]] > limit:
                            ret[0] += inf
                            return   
                        else:
                            ret[0] += 1                     
                    else:                   
                        if partial_sum[links[node][0]]>partial_sum[links[node][1]]:
                            partial_sum[node] -= partial_sum[links[node][0]]
                            if partial_sum[links[node][0]] > limit:
                                ret[0] += inf
                                return 
                            else:
                                ret[0] += 1
                            if partial_sum[node]>limit:
                                partial_sum[node] -= partial_sum[links[node][1]]
                                if partial_sum[links[node][1]] > limit:
                                    ret[0] += inf
                                else:
                                    ret[0] += 1
                        else:
                            partial_sum[node] -= partial_sum[links[node][1]]
                            if partial_sum[links[node][1]] > limit:
                                ret[0] += inf 
                                return
                            else:
                                ret[0] += 1
                            if partial_sum[node]>limit:
                                partial_sum[node] -= partial_sum[links[node][0]]
                                if partial_sum[links[node][0]] > limit:
                                    ret[0] += inf
                                    return
                                else:
                                    ret[0] += 1
        if partial_sum[node] > limit:
            ret[0] += inf
            return 
        else:
            ret[0] += 1
                    
    check = [1 for i in range(len(links))]     
    for link in links:
        if link[0]!=-1:
            check[link[0]] = 0
        if link[1]!=-1:
            check[link[1]] = 0
                    
    head = None
    for i in range(len(check)):
        if check[i]:
            head = i
            break
        
    visit = [head]
    nodes = {0:[head]}
    cnt = 1
    while visit:
        tmp = []
        nodes[cnt] = []
        for v in visit:
            if links[v][0]!=-1:
                nodes[cnt].append(links[v][0])
                tmp.append(links[v][0])
            if links[v][1]!=-1:
                nodes[cnt].append(links[v][1])
                tmp.append(links[v][1])
        visit = tmp
        cnt += 1
    
    max_depth = max(nodes.keys())
    del nodes[max_depth]
    max_depth -= 1    
    
    def binary_search(s, e, links, nodes, max_depth, k, num):
        if s>=e:
            return s
        partial_sum = num[:]
        ret = [0]
        mid = (s+e)//2
        count(mid, links, partial_sum, nodes, max_depth, ret=ret)
        if ret[0]>k:
            return binary_search(mid+1, e, links, nodes, max_depth, k, num)
        else:
            return binary_search(s, mid, links, nodes, max_depth, k, num)
    
    answer = binary_search(1, sum(num)+1, links, nodes, max_depth, k, num)
    return answer

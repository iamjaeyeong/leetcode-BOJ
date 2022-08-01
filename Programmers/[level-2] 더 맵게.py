import heapq

def solution(scoville, K):
    answer = 0    
    h = []
    for i in scoville:
        if i<K:
            heapq.heappush(h, i)
    is_left = len(h)==len(scoville)
    
    if len(h)==0:
        return 0
    
    cnt = 0
    while 1:
        if len(h)<2 or h[0]>=K:
            break
        else:
            m1, m2 = heapq.heappop(h), heapq.heappop(h)
            heapq.heappush(h, m1 + 2 * m2)
            cnt += 1
    
    if h[0]>=K:
        return cnt
    elif is_left:
        return -1
    else:
        return cnt + 1
    
    return answer
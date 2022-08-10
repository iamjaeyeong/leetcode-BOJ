from collections import deque

def solution(n, edge):
    answer = 0
    edge_dict = {i:[] for i in range(n)}
    for e in edge:
        edge_dict[e[0]-1].append(e[1]-1)
        edge_dict[e[1]-1].append(e[0]-1)
        
    distance = [n+1 for i in range(n)]
    distance[0] = 1
    
    visit = deque([0])
    while visit:
        depart = visit.popleft()
        for dest in edge_dict[depart]:
            if distance[dest]<=distance[depart]+1:
                continue
            else:
                distance[dest] = distance[depart]+1
                visit.append(dest)

    farest = max(distance)
    for d in distance:
        if d==farest:
            answer += 1
    return answer
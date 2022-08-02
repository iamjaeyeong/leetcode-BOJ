import heapq

def solution(array, commands):
    answer = []
    
    for command in commands:
        heap = []
        for i in range(command[0]-1, command[1]):
            heapq.heappush(heap, array[i])
        for i in range(command[2]):
            pop = heapq.heappop(heap)
        answer.append(pop)
            
    
    return answer
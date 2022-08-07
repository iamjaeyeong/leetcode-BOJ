from collections import deque

class Solution:
    def merge(self, intervals):
        answer = []
        intervals.sort(key=lambda x:x[0])
        deq = deque(intervals)
        deq.append([100000, 100000])
        head = deq.popleft()
        
        for interval in deq:
            if head[1]>=interval[0]:
                head[1] = max(head[1], interval[1])
            elif head[1]<interval[0]:
                answer.append(head)
                head = interval
            else:
                answer.append(head)
        return answer
        
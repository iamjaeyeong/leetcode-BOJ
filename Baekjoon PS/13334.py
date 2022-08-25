import sys, heapq
input = sys.stdin.readline

r = []
n = int(input())
pos = []
for i in range(n):
    p = list(map(int, input().split()))
    pos.append([min(p), max(p)])
d = int(input())

for i in range(n):
    if pos[i][1]-d>pos[i][0]:
        continue
    else:
        r.append([pos[i][0], pos[i][1]-d])
  
r.sort(key=lambda x: x[1])      
heap = []
answer = 0
for i in range(len(r)):
    heapq.heappush(heap, r[i])
    while 1:
        if len(heap)==0 or heap[0][0]>=r[i][1]:
            break
        else:
            heapq.heappop(heap)
    answer = max(answer, len(heap))
    
print(answer)


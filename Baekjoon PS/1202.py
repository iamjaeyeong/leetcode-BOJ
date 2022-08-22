import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []
for i in range(n):
    jewel = list(map(int, input().split()))
    jewels.append((jewel[1]*(-1), jewel[0]))
    
jewels.sort(key = lambda x : x[1])

bags = []
for i in range(k):
    bags.append(int(input()))
bags.sort()

heap = []
idx = 0
answer = 0
for bag in bags:
    while 1:
        if idx>=len(jewels) or jewels[idx][1]>bag:
            break
        else:
            heapq.heappush(heap, jewels[idx])
            idx += 1
    if len(heap)==0:
        continue
    jewel = heapq.heappop(heap)
    answer -= jewel[0]
            
print(answer)

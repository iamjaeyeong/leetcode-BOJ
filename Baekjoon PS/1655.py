import sys, heapq
input=sys.stdin.readline
heappush=heapq.heappush
heappop=heapq.heappop


n=int(input())
dump_heap=[]
heap=[]
for i in range(n):
    m=int(input())
    if i!=0 and i%2==0:
        heappush(heap, m)
        tmp=heappop(heap)
        heappush(dump_heap, (-tmp, tmp))
    elif i%2==1 and m<heap[0]:
        heappush(dump_heap, (-m, m))
        again=heappop(dump_heap)[1]
        heappush(heap, again)
    else:
        heappush(heap, m)
    print(heap[0])
        

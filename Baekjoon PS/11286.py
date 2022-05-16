import sys, heapq
input=sys.stdin.readline

heappush=heapq.heappush
heappop=heapq.heappop

n=int(input())
heap=[]
for i in range(n):
    tmp=int(input())
    if tmp==0:
        if len(heap)==0:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        if tmp<0:
            tmp=(abs(tmp)-0.5, tmp)
        else:
            tmp=(abs(tmp), tmp)
        heappush(heap, tmp)

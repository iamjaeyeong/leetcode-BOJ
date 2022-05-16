import sys
input=sys.stdin.readline

def heap_pop(heap):
    idx=1
    while(1):
        if len(heap)-1<idx*2:
            heap[idx]=heap[-1]
            del heap[-1]
            if len(heap)>1 and idx<len(heap):
                heap_maximize(heap, idx)
            break
        elif len(heap)-1==idx*2:
            heap[idx]=heap[idx*2]
            del heap[idx*2]
            break
        else:
                if heap[idx*2]>heap[idx*2+1]:
                    heap[idx]=heap[idx*2]
                    idx*=2
                else:
                    heap[idx]=heap[idx*2+1]
                    idx=idx*2+1

def heap_maximize(heap, idx):
    while(idx>1):
        if heap[idx//2]<heap[idx]:
            tmp=heap[idx//2]
            heap[idx//2]=heap[idx]
            heap[idx]=tmp
            idx=idx//2
        else:
            break

n=int(input())
heap=[None]
for i in range(n):
    m=int(input())
    if m==0:
        if len(heap)>1:
            print(heap[1])
            heap_pop(heap)
        else:
            print(0)
    else:
        heap.append(m)
        heap_maximize(heap, len(heap)-1)

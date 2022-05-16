import sys
input=sys.stdin.readline

def heappop(heap):
    idx=1
    while(1):
        if idx*2>len(heap)-1:
            heap[idx]=heap[-1]
            del heap[-1]
            if idx>len(heap)-1:
                break
            else:
                heapify(heap, idx)
                break
        elif idx*2==len(heap)-1:
            heap[idx]=heap[idx*2]
            del heap[idx*2]
            break
        else:
            if heap[idx*2]<heap[idx*2+1]:
                heap[idx]=heap[idx*2]
                idx=idx*2
            else:
                heap[idx]=heap[idx*2+1]
                idx=idx*2+1

def heapify(heap, idx):
    while(1):
        if idx<2:
            break
        else:
            if heap[idx//2]>heap[idx]:
                tmp=heap[idx]
                heap[idx]=heap[idx//2]
                heap[idx//2]=tmp
                idx=idx//2
            else:
                break

n=int(input())
heap=[None]
for i in range(n):
    m=int(input())
    if m==0:
        if len(heap)<2:
            print(0)
        else:
            print(heap[1])
            heappop(heap)
    else:
        heap.append(m)
        heapify(heap, len(heap)-1)
        
    
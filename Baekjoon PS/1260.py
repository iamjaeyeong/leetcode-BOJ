from collections import deque
import sys, random, time
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
def find(lst, i, start, end):
    if start==end:
        if lst[start]==i:
            return 1
        else:
            return 0
    elif start>end:
        return 0
    else:
        mid=(start+end)//2
        if i>lst[mid]:
            return find(lst, i, mid+1, end)
        elif i<lst[mid]:
            return find(lst, i, start, mid-1)
        else:
            return 1


node, line, start=map(int, input().split())
connection=[]
for i in range(line):
    connection.append(list(map(int, input().split())))
start_2=start
connections={i:[] for i in range(1, node+1)}
for i in connection:
    connections[i[0]].append(i[1])
for i in connection:
    connections[i[1]].append(i[0])
for i in connections:
    connections[i].sort()
bfs_list=[]
dfs_list=[]
deq=deque()

deq.append(start)
while(1):
    for i in connections[start]:
        if i in deq or i in bfs_list:
            continue
        else:
            deq.append(i)
    bfs_list.append(deq.popleft())
    if len(deq)==0:
        break
    start=deq[0]


start=start_2
stack=deque()
stack.append(start)
past=[0 for i in range(1001)]
past[start]=1

def dfs(node, connections, stack, past, ret=[]):
    if stack==[]:
        ret.append(stack[-1])
        print(*ret)
    ret.append(stack[-1])        
    for i in connections[stack[-1]]:
        if past[i]==1:
            continue
        else:
            stack.append(i)
            past[i]=1
            dfs(node, connections, stack, past, ret=ret)
    stack.pop()

dfs(node, connections, stack, past, ret=dfs_list)
print(*dfs_list)
print(*bfs_list)


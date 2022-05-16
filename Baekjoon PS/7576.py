import sys
from collections import deque
input=sys.stdin.readline

m, n=map(int, input().split())
box=[]
for i in range(n):
    box.append(list(map(int, input().split())))
cnt=0
ripening=deque()
ripening.append(deque())
ripening.append(deque())

for i in range(n):
    for j in range(m):
        if box[i][j]==1:
            ripening[0].append([i, j])
while(1):
    if len(ripening[0])==0:
        if len(ripening[1])==0:
            break
        ripening.popleft()
        ripening.append(deque())
        cnt+=1
    pos=ripening[0].popleft()
    if pos[0]>0 and box[pos[0]-1][pos[1]]==0:
        box[pos[0]-1][pos[1]]=1
        ripening[1].append([pos[0]-1, pos[1]])
    if pos[1]>0 and box[pos[0]][pos[1]-1]==0:
        box[pos[0]][pos[1]-1]=1
        ripening[1].append([pos[0], pos[1]-1])
    if pos[0]<n-1 and box[pos[0]+1][pos[1]]==0:
        box[pos[0]+1][pos[1]]=1
        ripening[1].append([pos[0]+1, pos[1]])
    if pos[1]<m-1 and box[pos[0]][pos[1]+1]==0:
        box[pos[0]][pos[1]+1]=1
        ripening[1].append([pos[0], pos[1]+1])
all_ripen=1
for i in range(n):
    for j in range(m):
        if box[i][j]==0:
            all_ripen=0
            break
if all_ripen:
    print(cnt)
else:
    print(-1)
    
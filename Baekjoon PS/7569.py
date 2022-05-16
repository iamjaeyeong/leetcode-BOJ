import sys
from collections import deque
input=sys.stdin.readline

m, n, h=map(int, input().split())
box=[]
for _ in range(h):
    tmp=[]
    for i in range(n):
        tmp.append(list(map(int, input().split())))
    box.append(tmp)

cnt=0
ripening=deque()
ripening.append(deque())
ripening.append(deque())

for p in range(h):
    for i in range(n):
        for j in range(m):
            if box[p][i][j]==1:
                ripening[0].append([p, i, j])
while(1):
    if len(ripening[0])==0:
        if len(ripening[1])==0:
            break
        ripening.popleft()
        ripening.append(deque())
        cnt+=1
    pos=ripening[0].popleft()
    if pos[0]>0 and box[pos[0]-1][pos[1]][pos[2]]==0:
        box[pos[0]-1][pos[1]][pos[2]]=1
        ripening[1].append([pos[0]-1, pos[1], pos[2]])
    if pos[1]>0 and box[pos[0]][pos[1]-1][pos[2]]==0:
        box[pos[0]][pos[1]-1][pos[2]]=1
        ripening[1].append([pos[0], pos[1]-1, pos[2]])
    if pos[2]>0 and box[pos[0]][pos[1]][pos[2]-1]==0:
        box[pos[0]][pos[1]][pos[2]-1]=1
        ripening[1].append([pos[0], pos[1], pos[2]-1])
    if pos[0]<h-1 and box[pos[0]+1][pos[1]][pos[2]]==0:
        box[pos[0]+1][pos[1]][pos[2]]=1
        ripening[1].append([pos[0]+1, pos[1],pos[2]])
    if pos[1]<n-1 and box[pos[0]][pos[1]+1][pos[2]]==0:
        box[pos[0]][pos[1]+1][pos[2]]=1
        ripening[1].append([pos[0], pos[1]+1, pos[2]])
    if pos[2]<m-1 and box[pos[0]][pos[1]][pos[2]+1]==0:
        box[pos[0]][pos[1]][pos[2]+1]=1
        ripening[1].append([pos[0], pos[1], pos[2]+1])        
all_ripen=1
for p in range(h):
    for i in range(n):
        for j in range(m):
            if box[p][i][j]==0:
                all_ripen=0
                break
if all_ripen:
    print(cnt)
else:
    print(-1)
    
import sys
sys.setrecursionlimit(99999)

n = int(input())
answer = []

def next_pos(board, pos):
    ret = []
    if pos[0]!=0 and board[pos[0]-1][pos[1]]!='*':
        ret.append([pos[0]-1, pos[1]])
    if pos[1]!=0 and board[pos[0]][pos[1]-1]!='*':
        ret.append([pos[0], pos[1]-1])
    if pos[0]<len(board)-1 and board[pos[0]+1][pos[1]]!='*':
        ret.append([pos[0]+1, pos[1]])
    if pos[1]<len(board[0])-1 and board[pos[0]][pos[1]+1]!='*':
        ret.append([pos[0], pos[1]+1])
    return ret




def bfs(board, check, visits, ret=[[], [], 0], door_visit=False):
    if door_visit:
        next_visit = []
        for visit in visits:
            next_visit.extend(next_pos(board, visit))
        bfs(board, check, next_visit, ret=ret)
    else:
        next_visit = []
        for visit in visits:
            next = 0
            if check[visit[0]][visit[1]]:
                continue
            else:
                check[visit[0]][visit[1]] = 1
                
            if board[visit[0]][visit[1]]=='*':
                continue
            elif board[visit[0]][visit[1]]=="$":
                ret[2] += 1
                next = 1
            elif board[visit[0]][visit[1]]==".":
                next = 1
            elif 65<=ord(board[visit[0]][visit[1]])<=90:
                ret[0].append(visit)
            else:
                ret[1].append(board[visit[0]][visit[1]])
                next = 1
            if next:
                next_visit.extend(next_pos(board, visit))
        if next_visit:
            bfs(board, check, next_visit, ret=ret)
            
        
    # door 발견
    # key 발견
    # 서류 발견
    

def main():
    h, w = map(int, input().split())
    board = []
    for i in range(h):
        row = input()
        board.append([i for i in row])
    keys = input()
    check = [[0 for i in range(w)] for j in range(h)]    
    entrances = []
    papers = 0
    doors_pos = {}
    
    if keys=='0\n':
        keys = set()
    else:
        keys = set(i for i in keys) 
    initial_pos = []
    for i in range(w):
        initial_pos.append([0, i])
        initial_pos.append([h-1, i])
    for i in range(1, h-1):
        initial_pos.append([i, 0])
        initial_pos.append([i, w-1])
    for i in initial_pos:
        if board[i[0]][i[1]]=='*':
            continue
        elif board[i[0]][i[1]]=='.' or board[i[0]][i[1]]=='$':
            entrances.append(i)
        elif 65<=ord(board[i[0]][i[1]])<=90:
            if chr(ord(board[i[0]][i[1]])+32) in keys:
                board[i[0]][i[1]] = '.'
                entrances.append(i)
            elif board[i[0]][i[1]] in doors_pos:
                    doors_pos[board[i[0]][i[1]]].add((i[0], i[1]))
            else:
                doors_pos[board[i[0]][i[1]]] = set()
                doors_pos[board[i[0]][i[1]]].add((i[0], i[1]))
                
        elif 97<=ord(board[i[0]][i[1]])<=122:
            entrances.append(i)
            
    ret = [[], [], 0]
    bfs(board, check, entrances, ret=ret)
    papers += ret[-1]
    
    while 1:
        if len(ret[0])==0 and len(ret[1])==0:
            break    
        visits = []
        for key in ret[1]:
            keys.add(key)
        for pos in ret[0]:
            if board[pos[0]][pos[1]] in doors_pos:
                doors_pos[board[pos[0]][pos[1]]].add((pos[0], pos[1]))
            else:
                doors_pos[board[pos[0]][pos[1]]] = set()
                doors_pos[board[pos[0]][pos[1]]].add((pos[0], pos[1]))
        dump = []
        for key in keys:
            door = chr(ord(key)-32)
            if door not in doors_pos:
                continue
            for open in doors_pos[door]:
                visits.append([open[0], open[1]])
                board[open[0]][open[1]] = '.'
                dump.append([door, open])
        for door, d in dump:
            doors_pos[door].discard(d)
        ret = [[], [], 0]
        bfs(board, check, visits, ret, door_visit=True)
        papers += ret[-1]
    return papers
    
for i in range(n):
    answer.append(main())

for i in answer:
    print(i)
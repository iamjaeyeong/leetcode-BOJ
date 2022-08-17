def solution(places):
    answer = []
    def find(room, check, pos, n_move, ret=[]):
        if n_move>2:
            return
        elif pos[0]<0 or pos[1]<0 or pos[0]>4 or pos[1]>4:
            return
        elif room[pos[0]][pos[1]]=='X' or check[pos[0]][pos[1]]:
            return
        elif n_move!=0 and room[pos[0]][pos[1]]=='P':
            ret[0] = 1
            return
        else:
            check[pos[0]][pos[1]] = 1
            find(room, check, [pos[0]+1, pos[1]], n_move+1, ret=ret)
            find(room, check, [pos[0], pos[1]+1], n_move+1, ret=ret)
            find(room, check, [pos[0]-1, pos[1]], n_move+1, ret=ret)
            find(room, check, [pos[0], pos[1]-1], n_move+1, ret=ret)
    
    for room in places:
        invalid = 0
        for col in range(5):
            for row in range(5):
                if room[col][row]=='P':      
                    ret = [0]
                    check = [[0 for i in range(5)] for j in range(5)]
                    find(room, check, [col, row], 0, ret=ret)
                    if ret[0]:
                        invalid = 1
                        break
            if invalid:
                break
        if invalid:
            answer.append(0)
        else:
            answer.append(1)
        
    return answer

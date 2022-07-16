def solution(board, moves):
    answer = 0
    bucket = [-1]
    for move in moves:
        doll = 0
        for i in range(len(board)):
            if board[i][move-1]:
                doll = board[i][move-1]
                board[i][move-1] = 0
                break
        if doll:
            if bucket[-1]==doll:
                answer += 1
                bucket.pop()
            else:
                bucket.append(doll)
            
    
    return answer*2
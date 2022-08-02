class Solution:
    def spiralOrder(self, matrix):
        spider = [0, 0]
        move_type = ['right', 'down', 'left', 'up']
        answer = []
        answer.append(matrix[0][0])
        matrix[0][0] = None
        while len(answer)!=len(matrix)*len(matrix[0]):
            for move in move_type:
                if move=='right':
                    while 1:
                        if spider[1]+1>=len(matrix[0]) or matrix[spider[0]][spider[1]+1]==None:
                            break
                        spider[1] += 1
                        answer.append(matrix[spider[0]][spider[1]])
                        matrix[spider[0]][spider[1]] = None
                elif move=='down':
                    while 1:
                        if spider[0]+1>=len(matrix) or matrix[spider[0]+1][spider[1]]==None:
                            break
                        spider[0] += 1
                        answer.append(matrix[spider[0]][spider[1]])
                        matrix[spider[0]][spider[1]] = None
                elif move=='left':
                    while 1:
                        if spider[0]-1<0 or matrix[spider[0]-1][spider[1]]==None:
                            break
                        spider[0] -= 1
                        answer.append(matrix[spider[0]][spider[1]])
                        matrix[spider[0]][spider[1]] = None
                else:                
                    while 1:
                        if spider[1]-1<0 or matrix[spider[0]][spider[1]-1]==None:
                            break
                        spider[1] -= 1
                        answer.append(matrix[spider[0]][spider[1]])
                        matrix[spider[0]][spider[1]] = None
        return answer
        
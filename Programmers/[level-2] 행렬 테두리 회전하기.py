def solution(rows, columns, queries):
    matrix = [[columns*row + col + 1 for col in range(columns)] for row in range(rows)]
    answer = []
    def rotation(matrix, querie, mx):
        next = matrix[querie[0]][querie[1]]
        mn = mx
        tmp = None
        for i in range(querie[1]+1, querie[3]+1):
            if mn>next:
                mn = next
            tmp = matrix[querie[0]][i]
            matrix[querie[0]][i] = next
            next = tmp
        for i in range(querie[0]+1, querie[2]+1):
            if mn>next:
                mn = next
            tmp = matrix[i][querie[3]]
            matrix[i][querie[3]] = next
            next = tmp
        for i in range(querie[3]-1, querie[1]-1, -1):
            if mn>next:
                mn = next
            tmp = matrix[querie[2]][i]
            matrix[querie[2]][i] = next
            next = tmp
        for i in range(querie[2]-1, querie[0]-1, -1):
            if mn>next:
                mn = next
            tmp = matrix[i][querie[1]]
            matrix[i][querie[1]] = next
            next = tmp
        return mn
    mx = matrix[-1][-1]
    for querie in queries:
        answer.append(rotation(matrix, [querie[0]-1, querie[1]-1, querie[2]-1, querie[3]-1], mx))

    return answer
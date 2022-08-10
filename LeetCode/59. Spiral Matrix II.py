class Solution:
    def generateMatrix(self, n: int):
        answer = [[0 for i in range(n)] for j in range(n)]
        pos = []
        spider = [0, 0]
        for i in range(n, 0, -2):
            for j in range(i):
                pos.append(spider[:])
                spider[1] += 1
            spider[1] -= 1
            spider[0] += 1
            for j in range(i-1):
                pos.append(spider[:])
                spider[0] += 1
            spider[0] -= 1
            spider[1] -= 1
            for j in range(i-1):
                pos.append(spider[:])
                spider[1] -= 1
            spider[1] += 1
            spider[0] -= 1
            for j in range(i-2):
                pos.append(spider[:])
                spider[0] -= 1
            spider[0] += 1
            spider[1] += 1
            
        for i, p in enumerate(pos):
            answer[p[0]][p[1]] = i + 1
            
        return answer
                

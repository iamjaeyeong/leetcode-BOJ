class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)//2):
            row1 = [[i, i+j] for j in range(len(matrix)-2*i-1)]
            row2 = [[len(matrix)-1-i, len(matrix)-1-i-j] for j in range(len(matrix)-2*i-1)]
            col1 = [[i+j, len(matrix)-1-i] for j in range(len(matrix)-2*i-1)]
            col2 = [[len(matrix)-1-i-j, i] for j in range(len(matrix)-2*i-1)]
            for j in range(len(col1)):
                tmp = [matrix[row1[j][0]][row1[j][1]], matrix[col1[j][0]][col1[j][1]], matrix[row2[j][0]][row2[j][1]], matrix[col2[j][0]][col2[j][1]]]
                matrix[col1[j][0]][col1[j][1]] = tmp[0]
                matrix[row2[j][0]][row2[j][1]] = tmp[1]
                matrix[col2[j][0]][col2[j][1]] = tmp[2]
                matrix[row1[j][0]][row1[j][1]] = tmp[3]
                
                
           
            

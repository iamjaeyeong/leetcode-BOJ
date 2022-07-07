class Solution:
    def isValidSudoku(self, board) -> bool:
        def init_check(lst):
            for i in range(9):
                lst[i] = 0
                
        row_check = [0 for i in range(9)]
        col_check = [0 for i in range(9)]
        box_check = [0 for i in range(9)]
        
        for row in board:
            init_check(row_check)
            for cell in row:
                if cell==".":
                    continue
                elif row_check[int(cell)-1]:
                    return False
                else:
                    row_check[int(cell)-1] = 1
        
        for col in range(9):
            init_check(col_check)
            for cell in range(9):
                cell = board[cell][col]
                if cell==".":
                    continue
                elif col_check[int(cell)-1]:
                    return False
                else:
                    col_check[int(cell)-1] = 1
        
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                init_check(box_check)
                for i in range(3):
                    for j in range(3):
                        cell = board[y+i][x+j]
                        if cell==".":
                            continue
                        elif box_check[int(cell)-1]:
                            return False
                        else:
                            box_check[int(cell)-1] = 1
        
        return True
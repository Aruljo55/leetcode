class Solution:
    def isValidSudoku(self, board):
        def isValidBlock(block):
            block = [num for num in block if num != '.']
            return len(block) == len(set(block))
        
        for row in board:
            if not isValidBlock(row):
                return False
        
        for col in zip(*board):
            if not isValidBlock(col):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                block = [
                    board[x][y]
                    for x in range(i, i + 3)
                    for y in range(j, j + 3)
                ]
                if not isValidBlock(block):
                    return False
        
        return True

class Solution:
    def solveSudoku(self, board):
        def is_valid(num, row, col):
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
                box_row = 3 * (row // 3) + i // 3
                box_col = 3 * (col // 3) + i % 3
                if board[box_row][box_col] == num:
                    return False
            return True

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(num, i, j):
                                board[i][j] = num
                                if backtrack():
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        backtrack()
if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    solution = Solution()
    solution.solveSudoku(board)
    print(board)

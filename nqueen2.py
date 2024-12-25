class Solution:
    def totalNQueens(self, n):
        def is_valid(board, row, col):
            for i in range(row):
                if board[i] == col or abs(board[i] - col) == abs(i - row):
                    return False
            return True

        def backtrack(row):
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1

        self.count = 0
        board = [-1] * n
        backtrack(0)
        return self.count

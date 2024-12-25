class Solution:
    def solveNQueens(self, n):
        def is_valid(board, row, col):
            for i in range(row):
                if board[i] == col or abs(board[i] - col) == abs(i - row):
                    return False
            return True

        def backtrack(row):
            if row == n:
                solution = []
                for i in range(n):
                    row_str = '.' * board[i] + 'Q' + '.' * (n - board[i] - 1)
                    solution.append(row_str)
                result.append(solution)
                return
            for col in range(n):
                if is_valid(board, row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1

        result = []
        board = [-1] * n
        backtrack(0)
        return result

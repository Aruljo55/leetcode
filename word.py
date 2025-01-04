class Solution:
    def exist(self, board, word):
        def backtrack(i, j, k):
            # Check if out of bounds or character doesn't match
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            # Check if we've matched the entire word
            if k == len(word) - 1:
                return True
            
            # Temporarily mark the cell as visited
            temp = board[i][j]
            board[i][j] = "#"
            
            # Explore neighbors (up, down, left, right)
            found = (
                backtrack(i + 1, j, k + 1) or
                backtrack(i - 1, j, k + 1) or
                backtrack(i, j + 1, k + 1) or
                backtrack(i, j - 1, k + 1)
            )
            
            # Restore the cell after exploring
            board[i][j] = temp
            
            return found
        
        m, n = len(board), len(board[0])
        
        # Try to find the word starting from each cell
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False

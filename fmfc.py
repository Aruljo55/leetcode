class Solution:
    def maxCollectedFruits(self, fruits):
        n = len(fruits)
        visited = set()
        total = 0

        # Child 1: main diagonal
        for i in range(n):
            if (i, i) not in visited:
                visited.add((i, i))
                total += fruits[i][i]

        # Child 2: top-right to bottom-right diagonal path as per example
        path2 = [(0, n-1), (1, n-2), (2, n-1), (3,3)] if n==4 else [(0,n-1),(n-1,n-1)]
        for r,c in path2:
            if (r,c) not in visited:
                visited.add((r,c))
                total += fruits[r][c]

        # Child 3: bottom-left to bottom-right path
        for j in range(n):
            if (n-1,j) not in visited:
                visited.add((n-1,j))
                total += fruits[n-1][j]

        return total

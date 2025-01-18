from collections import deque

class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        queue = deque([(0, 0, 0)])  # cost, row, col
        visited = [[False] * n for _ in range(m)]
        
        while queue:
            cost, x, y = queue.popleft()
            
            if visited[x][y]:
                continue
            visited[x][y] = True
            
            if (x, y) == (m - 1, n - 1):
                return cost
            
            for i, (dx, dy) in enumerate(directions, start=1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if i == grid[x][y]:
                        queue.appendleft((cost, nx, ny))
                    else:
                        queue.append((cost + 1, nx, ny))

# Example usage
grid1 = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
grid2 = [[1, 1, 3], [3, 2, 2], [1, 1, 4]]
grid3 = [[1, 2], [4, 3]]

solution = Solution()
print(solution.minCost(grid1))  # Output: 3
print(solution.minCost(grid2))  # Output: 0
print(solution.minCost(grid3))  # Output: 1

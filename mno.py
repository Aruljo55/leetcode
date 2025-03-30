from collections import deque

class Solution:
    def maxPoints(self, grid, queries):
        m, n = len(grid), len(grid[0])
        
        # Directions for moving in 4 directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Sort the unique values in the grid
        unique_values = sorted(set(cell for row in grid for cell in row))
        
        # A dictionary to store the maximum points for each threshold
        points_for_threshold = {}
        
        # Function to perform BFS to explore the grid and calculate points
        def bfs(threshold):
            visited = [[False] * n for _ in range(m)]
            queue = deque([(0, 0)])  # Start from the top-left corner
            visited[0][0] = True
            points = 0
            
            while queue:
                x, y = queue.popleft()
                if grid[x][y] < threshold:
                    points += 1
                # Explore adjacent cells
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] < threshold:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            
            return points
        
        # For each unique value in the grid, calculate the max points that can be collected
        current_threshold_idx = 0
        max_points = 0
        for value in unique_values:
            # Calculate points for this threshold
            if value > grid[0][0]:  # only perform BFS if the threshold is greater than the top-left value
                max_points = bfs(value)
            points_for_threshold[value] = max_points
        
        # For each query, get the maximum points based on the precomputed thresholds
        answer = []
        for query in queries:
            if query in points_for_threshold:
                answer.append(points_for_threshold[query])
            else:
                # Return the closest threshold that will be stored value.
                answer.append(0)
        return answer


# Test example
grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
queries = [5, 6, 2]
solution = Solution()
print(solution.maxPoints(grid, queries))  # Expected Output: [5, 8, 1]

grid2 = [[5, 2, 1], [1, 1, 2]]
queries2 = [3]
solution2 = Solution()
print(solution2.maxPoints(grid2, queries2))  # Expected Output: [0]

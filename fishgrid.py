class Solution:
    def findMaxFish(self, grid):
        def bfs(start_r, start_c):
            queue = deque([(start_r, start_c)])
            visited[start_r][start_c] = True
            total_fish = 0

            while queue:
                r, c = queue.popleft()
                total_fish += grid[r][c]
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] > 0:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            
            return total_fish

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_fish = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0 and not visited[r][c]:
                    max_fish = max(max_fish, bfs(r, c))

        return max_fish

class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        parent = [i for i in range(n * n)]
        size = [1] * (n * n)
        
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        
        def union(u, v):
            u_root = find(u)
            v_root = find(v)
            if u_root == v_root:
                return
            if size[u_root] < size[v_root]:
                u_root, v_root = v_root, u_root
            parent[v_root] = u_root
            size[u_root] += size[v_root]
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            union(i * n + j, x * n + y)
        
        max_size = max(size)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    unique_roots = set()
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            unique_roots.add(find(x * n + y))
                    total = 1
                    for root in unique_roots:
                        total += size[root]
                    max_size = max(max_size, total)
        
        return max_size
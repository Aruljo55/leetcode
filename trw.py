import heapq

class Solution:
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])

        if m < 3 or n < 3:
            return 0

        visited = [[False]*n for _ in range(m)]
        heap = []

        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited[i][0] = True
            visited[i][n-1] = True

        for j in range(1, n-1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited[0][j] = True
            visited[m-1][j] = True

        water = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            h, x, y = heapq.heappop(heap)
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    nh = heig

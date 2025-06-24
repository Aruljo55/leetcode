import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # (time, x, y)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            time, x, y = heapq.heappop(heap)
            if (x, y) == (n - 1, m - 1):
                return time
            if time > dist[x][y]:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    next_time = time + 1
                    if next_time < moveTime[nx][ny]:
                        wait = moveTime[nx][ny] - next_time
                        # If wait is odd, add 1 to make it even
                        if wait % 2 == 1:
                            wait += 1
                        next_time += wait
                    if next_time < dist[nx][ny]:
                        dist[nx][ny] = next_time
                        heapq.heappush(heap, (next_time, nx, ny))
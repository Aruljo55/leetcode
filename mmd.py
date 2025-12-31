from collections import deque

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        n = len(s)
        queue = deque()
        queue.append((0, 0, 0, 0))  # x, y, index, changes used
        visited = set()
        max_dist = 0

        while queue:
            x, y, i, changes = queue.popleft()
            max_dist = max(max_dist, abs(x) + abs(y))
            if i == n or (x, y, i, changes) in visited or changes > k:
                continue
            visited.add((x, y, i, changes))
            
            # Option 1: don't change current character
            dx, dy = directions[s[i]]
            queue.append((x + dx, y + dy, i + 1, changes))

            # Option 2: change current character to any of the 3 other directions
            if changes < k:
                for d in directions:
                    if d != s[i]:
                        dx, dy = directions[d]
                        queue.append((x + dx, y + dy, i + 1, changes + 1))
        
        return max_dist

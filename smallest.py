from collections import defaultdict, deque

class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= limit:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False] * n
        result = nums[:]

        for i in range(n):
            if not visited[i]:
                component = []
                queue = deque([i])
                visited[i] = True

                while queue:
                    node = queue.popleft()
                    component.append(node)

                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)

                indices = sorted(component)
                values = sorted(nums[j] for j in component)

                for idx, value in zip(indices, values):
                    result[idx] = value

        return result
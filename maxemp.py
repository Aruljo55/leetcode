class Solution:
    def maximumInvitations(self, favorite):
        n = len(favorite)
        indegree = [0] * n
        for f in favorite:
            indegree[f] += 1

        queue = [i for i in range(n) if indegree[i] == 0]
        longest_chain = [0] * n

        while queue:
            node = queue.pop()
            next_node = favorite[node]
            longest_chain[next_node] = max(longest_chain[next_node], longest_chain[node] + 1)
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)

        visited = [False] * n
        max_cycle = 0
        cycle_pairs = 0

        for i in range(n):
            if not visited[i]:
                current = i
                cycle_length = 0
                stack = []
                while not visited[current]:
                    visited[current] = True
                    stack.append(current)
                    current = favorite[current]

                if current in stack:
                    cycle_start = stack.index(current)
                    cycle_length = len(stack) - cycle_start
                    if cycle_length == 2:
                        a, b = stack[cycle_start], stack[cycle_start + 1]
                        cycle_pairs += 2 + longest_chain[a] + longest_chain[b]
                    else:
                        max_cycle = max(max_cycle, cycle_length)

        return max(max_cycle, cycle_pairs)

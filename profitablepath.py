class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = {0: -1}
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if nei not in parent:
                    parent[nei] = node
                    queue.append(nei)

        bob_path = set()
        curr = bob
        steps_bob = 0
        while curr != -1:
            bob_path.add((curr, steps_bob))
            curr = parent[curr]
            steps_bob += 1

        res = float('-inf')

        def dfs(node, curr_sum, steps_alice):
            nonlocal res
            shared = next((steps_bob for n, steps_bob in bob_path if n == node), None)

            if shared is not None:
                if shared == steps_alice:
                    curr_sum += amount[node] // 2
                elif shared > steps_alice:
                    curr_sum += amount[node]
            else:
                curr_sum += amount[node]

            if len(graph[node]) == 1 and node != 0:
                res = max(res, curr_sum)

            for nei in graph[node]:
                if nei != parent.get(node, -1):
                    dfs(nei, curr_sum, steps_alice + 1)

        dfs(0, 0, 0)
        return res

import heapq

class Solution:
    def minimumCost(self, n, edges, queries):
        graph = [[] for _ in range(n)]
        
        # Building the graph
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Helper function for BFS
        def bfs(start, end):
            # Priority queue stores the (current_cost, node)
            pq = [(-1 << 30, start)]  # max value to start, node
            min_cost = [-1] * n
            min_cost[start] = (1 << 30) - 1  # We start with the max possible AND value
            
            while pq:
                cost, node = heapq.heappop(pq)
                cost = -cost  # Convert back from negative for max-heap behavior
                
                # If we reached the target node, return the cost
                if node == end:
                    return cost
                
                for neighbor, weight in graph[node]:
                    new_cost = cost & weight
                    # If we found a better AND value for the neighbor, we update and push it into the heap
                    if new_cost > min_cost[neighbor]:
                        min_cost[neighbor] = new_cost
                        heapq.heappush(pq, (-new_cost, neighbor))
            
            return -1
        
        # Process each query
        result = []
        for s, t in queries:
            result.append(bfs(s, t))
        
        return result

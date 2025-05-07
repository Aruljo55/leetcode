from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)
        
        route = []

        def visit(airport):
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                visit(next_airport)
            route.append(airport)

        visit("JFK")
        return route[::-1]

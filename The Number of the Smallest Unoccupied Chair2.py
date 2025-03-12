import heapq

class Solution:
    def smallestChair(self, times, targetFriend):
        n = len(times)
        arrivals = sorted([(times[i][0], i) for i in range(n)])
        leaves = []
        available_chairs = []
        chair_map = {}
        
        for arrival, friend in arrivals:
            while leaves and leaves[0][0] <= arrival:
                _, chair = heapq.heappop(leaves)
                heapq.heappush(available_chairs, chair)
            
            chair = heapq.heappop(available_chairs) if available_chairs else len(chair_map)
            chair_map[friend] = chair
            heapq.heappush(leaves, (times[friend][1], chair))
            
            if friend == targetFriend:
                return chair

# Example Test Cases
solution = Solution()
print(solution.smallestChair([[1,4],[2,3],[4,6]], 1))  # Output: 1
print(solution.smallestChair([[3,10],[1,5],[2,6]], 0))  # Output: 2

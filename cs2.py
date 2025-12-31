from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque([course for course in indegree if indegree[course] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return order if len(order) == numCourses else []

# Example usage
solution = Solution()
print(solution.findOrder(numCourses=2, prerequisites=[[1, 0]]))  # Output: [0, 1]
print(solution.findOrder(numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))  # Output: [0, 2, 1, 3]
print(solution.findOrder(numCourses=1, prerequisites=[]))  # Output: [0]

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque([course for course in in_degree if in_degree[course] == 0])
        taken_courses = 0
        
        while queue:
            course = queue.popleft()
            taken_courses += 1
            
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return taken_courses == numCourses

# Example usage:
solution = Solution()
print(solution.canFinish(2, [[1,0]]))  # Output: True
print(solution.canFinish(2, [[1,0],[0,1]]))  # Output: False

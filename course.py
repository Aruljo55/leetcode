class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = [[False] * numCourses for _ in range(numCourses)]

        for pre in prerequisites:
            graph[pre[0]][pre[1]] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if graph[i][k] and graph[k][j]:
                        graph[i][j] = True

        return [graph[u][v] for u, v in queries]
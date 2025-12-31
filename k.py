class Solution:
    def getHappyString(self, n, k):
        self.result = []
        self.chars = ['a', 'b', 'c']

        def backtrack(current):
            if len(current) == n:
                self.result.append(current)
                return

            for char in self.chars:
                if not current or char != current[-1]:
                    backtrack(current + char)

        backtrack("")
        self.result.sort()
        return self.result[k - 1] if k <= len(self.result) else ""

# Example usage
solution = Solution()
print(solution.getHappyString(n=3, k=9))
class Solution:
    def minLength(self, s):
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 2 and (stack[-2] + stack[-1] == "AB" or stack[-2] + stack[-1] == "CD"):
                stack.pop()
                stack.pop()
        return len(stack)

solution = Solution()
print(solution.minLength("ABFCACDB"))  # Output: 2
print(solution.minLength("ACBBD"))     # Output: 5

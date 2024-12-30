class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        prev1, prev2 = 2, 1

        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1

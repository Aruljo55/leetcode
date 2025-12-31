class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

# Example usage
solution = Solution()
print(solution.rangeBitwiseAnd(5, 7))  # Output: 4
print(solution.rangeBitwiseAnd(0, 0))  # Output: 0
print(solution.rangeBitwiseAnd(1, 2147483647))  # Output: 0

from bisect import bisect_right, bisect_left

class Solution:
    def maximumCount(self, nums):
        firstPositive = bisect_right(nums, 0)  # First positive number index
        firstZero = bisect_left(nums, 0)  # First zero index (or last negative + 1)
        
        neg = firstZero  # Number of negative numbers
        pos = len(nums) - firstPositive  # Number of positive numbers

        return max(pos, neg)

# Example Test Cases
solution = Solution()
print(solution.maximumCount([-2,-1,-1,1,2,3]))  # Output: 3
print(solution.maximumCount([-3,-2,-1,0,0,1,2]))  # Output: 3
print(solution.maximumCount([5,20,66,1314]))  # Output: 4

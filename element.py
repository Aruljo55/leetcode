class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

# Example usage
solution = Solution()
print(solution.majorityElement([3, 2, 3]))       # Output: 3
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2

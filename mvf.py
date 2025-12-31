class Solution:
    def maximumTripletValue(self, nums):
        n = len(nums)
        max_value = 0  # Initialize max_value to 0
        
        for i in range(n - 2):  # First element
            for j in range(i + 1, n - 1):  # Second element
                for k in range(j + 1, n):  # Third element
                    value = (nums[i] - nums[j]) * nums[k]
                    max_value = max(max_value, value)
        
        return max_value

# Test cases
sol = Solution()
print(sol.maximumTripletValue([12, 6, 1, 2, 7]))  # Output: 77
print(sol.maximumTripletValue([1, 10, 3, 4, 19]))  # Output: 133
print(sol.maximumTripletValue([1, 2, 3]))  # Output: 0

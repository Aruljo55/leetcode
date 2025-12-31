class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0

# Example usage
solution = Solution()
print(solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))  # Output: 2
print(solution.minSubArrayLen(target=4, nums=[1, 4, 4]))  # Output: 1
print(solution.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))  # Output: 0

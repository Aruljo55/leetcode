class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

# Example usage
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
print(solution.twoSum([2, 3, 4], 6))       # Output: [1, 3]
print(solution.twoSum([-1, 0], -1))        # Output: [1, 2]

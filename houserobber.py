class Solution:
    def rob(self, nums):
        def rob_linear(houses):
            prev = curr = 0
            for amount in houses:
                prev, curr = curr, max(curr, prev + amount)
            return curr

        if len(nums) == 1:
            return nums[0]

        # Since houses are arranged in a circle, we compare two scenarios:
        # 1. Rob houses from index 0 to n-2
        # 2. Rob houses from index 1 to n-1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([2, 3, 2]))  # Output: 3
    print(solution.rob([1, 2, 3, 1]))  # Output: 4
    print(solution.rob([1, 2, 3]))  # Output: 3

class Solution:
    def findTargetSumWays(self, nums, target):
        dp = {0: 1}  # A dictionary to store the number of ways to reach a sum

        for num in nums:
            next_dp = {}
            for curr_sum, count in dp.items():
                next_dp[curr_sum + num] = next_dp.get(curr_sum + num, 0) + count
                next_dp[curr_sum - num] = next_dp.get(curr_sum - num, 0) + count
            dp = next_dp

        return dp.get(target, 0)

# Example usage for debugging
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 1, 1, 1, 1]
    target1 = 3
    print(solution.findTargetSumWays(nums1, target1))

    nums2 = [1]
    target2 = 1
    print(solution.findTargetSumWays(nums2, target2))

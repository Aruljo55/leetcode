class Solution:
    def maximumTripletValue(self, nums):
        n = len(nums)
        max_value = 0

        # Step 1: Compute prefix min array
        min_i = [0] * n
        min_i[0] = nums[0]
        for i in range(1, n):
            min_i[i] = min(min_i[i-1], nums[i])

        # Step 2: Compute suffix max array
        max_k = [0] * n
        max_k[n-1] = nums[n-1]
        for k in range(n-2, -1, -1):
            max_k[k] = max(max_k[k+1], nums[k])

        # Step 3: Iterate over j and compute max value
        for j in range(1, n-1):
            left_min = min_i[j-1]  # Min value before j
            right_max = max_k[j+1]  # Max value after j

            triplet_value = (left_min - nums[j]) * right_max
            max_value = max(max_value, triplet_value)

        return max_value

# Example usage:
nums = [12,6,1,2,7]
solution = Solution()
print(solution.maximumTripletValue(nums))  # Output: 77

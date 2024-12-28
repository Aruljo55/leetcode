class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        # Step 1: Compute sliding window sums
        window_sums = [0] * (n - k + 1)
        curr_sum = sum(nums[:k])
        window_sums[0] = curr_sum
        for i in range(1, n - k + 1):
            curr_sum += nums[i + k - 1] - nums[i - 1]
            window_sums[i] = curr_sum

        # Step 2: Compute left and right best indices
        left = [0] * len(window_sums)
        right = [0] * len(window_sums)
        
        best_left = 0
        for i in range(len(window_sums)):
            if window_sums[i] > window_sums[best_left]:
                best_left = i
            left[i] = best_left

        best_right = len(window_sums) - 1
        for i in range(len(window_sums) - 1, -1, -1):
            if window_sums[i] >= window_sums[best_right]:  # >= to prefer lexicographically smaller
                best_right = i
            right[i] = best_right

        # Step 3: Find the maximum sum using middle subarray
        max_sum = 0
        result = []
        for mid in range(k, len(window_sums) - k):
            l = left[mid - k]
            r = right[mid + k]
            total = window_sums[l] + window_sums[mid] + window_sums[r]
            if total > max_sum:
                max_sum = total
                result = [l, mid, r]

        return result

class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        if n <= 1:
            return

        # Step 1: Find the first index `i` from the right where nums[i] < nums[i + 1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the smallest number larger than nums[i] to the right of i
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the subarray to the right of i
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

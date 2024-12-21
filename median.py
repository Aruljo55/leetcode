class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array to minimize the search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len + 1) // 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # Partition point in nums1
            j = half_len - i  # Corresponding partition point in nums2

            # Set boundaries for i and j
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]

            # Check if partition is correct
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # If total length is odd, return the max of the left side
                if total_len % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                # If total length is even, return the average of the middle two values
                return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2.0

            elif nums1_left_max > nums2_right_min:
                # Move the search space to the left
                right = i - 1
            else:
                # Move the search space to the right
                left = i + 1

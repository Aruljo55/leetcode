class Solution:
    def jump(self, nums):
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            # Update the farthest we can reach
            farthest = max(farthest, i + nums[i])

            # If we reach the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest

                # If the farthest point reaches or exceeds the last index, break
                if current_end >= n - 1:
                    break

        return jumps

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums1 = [2, 3, 1, 1, 4]
    nums2 = [2, 3, 0, 1, 4]

    print("Minimum jumps for nums1:", solution.jump(nums1))  # Output: 2
    print("Minimum jumps for nums2:", solution.jump(nums2))  # Output: 2

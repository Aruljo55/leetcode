import random

class Solution:
    def wiggleSort(self, nums):
        n = len(nums)

        # Step 1: Find the median
        def nth_element(nums, n):
            def select(left, right, k):
                pivot = nums[random.randint(left, right)]
                l, r = left, right
                while l <= r:
                    while nums[l] < pivot: l += 1
                    while nums[r] > pivot: r -= 1
                    if l <= r:
                        nums[l], nums[r] = nums[r], nums[l]
                        l += 1
                        r -= 1
                if k <= r:
                    return select(left, r, k)
                elif k >= l:
                    return select(l, right, k)
                return nums[k]
            return select(0, len(nums) - 1, n)

        median = nth_element(nums[:], len(nums) // 2)

        # Step 2: 3-way partition using virtual index
        def index(i):
            return (1 + 2 * i) % (n | 1)

        left, i, right = 0, 0, n - 1
        while i <= right:
            if nums[index(i)] > median:
                nums[index(i)], nums[index(left)] = nums[index(left)], nums[index(i)]
                i += 1
                left += 1
            elif nums[index(i)] < median:
                nums[index(i)], nums[index(right)] = nums[index(right)], nums[index(i)]
                right -= 1
            else:
                i += 1

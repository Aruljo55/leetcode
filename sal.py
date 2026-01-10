class Solution:
    def splitArray(self, nums, k):
        left = max(nums)
        right = sum(nums)

        def can_split(max_sum):
            count = 1
            curr = 0
            for n in nums:
                if curr + n <= max_sum:
                    curr += n
                else:
                    count += 1
                    curr = n
                    if count > k:
                        return False
            return True

        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1

        return left
arulimaa
class Solution:
    def countRangeSum(self, nums, lower, upper):
        def merge_sort(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = merge_sort(lo, mid) + merge_sort(mid, hi)
            j = k = mid
            for left in prefix[lo:mid]:
                while k < hi and prefix[k] - left < lower:
                    k += 1
                while j < hi and prefix[j] - left <= upper:
                    j += 1
                count += j - k
            # merge step
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        return merge_sort(0, len(prefix))

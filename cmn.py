class Solution:
    def maxNumber(self, nums1, nums2, k):
        def getMaxSubsequence(nums, t):
            stack = []
            drop = len(nums) - t
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:t]

        def merge(sub1, sub2):
            res = []
            while sub1 or sub2:
                # Choose the bigger remaining subsequence
                if sub1 > sub2:
                    res.append(sub1.pop(0))
                else:
                    res.append(sub2.pop(0))
            return res

        max_num = []
        m, n = len(nums1), len(nums2)

        for i in range(max(0, k - n), min(k, m) + 1):
            part1 = getMaxSubsequence(nums1, i)
            part2 = getMaxSubsequence(nums2, k - i)
            merged = merge(part1[:], part2[:])  # [:] to avoid modifying originals
            max_num = max(max_num, merged)
        
        return max_num

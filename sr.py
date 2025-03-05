class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        
        ranges = []
        start = nums[0]
        
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                if start == nums[i]:
                    ranges.append(str(start))
                else:
                    ranges.append(f"{start}->{nums[i]}")
                if i != len(nums) - 1:
                    start = nums[i + 1]
                    
        return ranges
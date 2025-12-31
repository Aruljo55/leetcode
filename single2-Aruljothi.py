class Solution:
    def singleNumber(self, nums):
        ones, twos = 0, 0
        
        for num in nums:
            # Update `ones` to track bits that appear exactly once
            ones = (ones ^ num) & ~twos
            # Update `twos` to track bits that appear exactly twice
            twos = (twos ^ num) & ~ones
        
        return ones

class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # Only start counting if num is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Continue to count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                longest = max(longest, current_length)
        
        return longest

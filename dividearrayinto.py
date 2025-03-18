class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        # Use Counter or create a frequency dictionary
        frequency = {}
        
        # Count the frequency of each number
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        # Check if each number appears an even number of times
        for count in frequency.values():
            if count % 2 != 0:
                return False
        
        return True
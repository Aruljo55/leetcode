class Solution:
    def minimumOperations(self, nums):
        operations = 0
        
        while True:
            seen = set()
            has_duplicate = False
            
            for num in nums:
                if num in seen:
                    has_duplicate = True
                    break
                seen.add(num)
            
            if not has_duplicate:
                break
            
            # Remove first 3 elements (or all if less than 3)
            nums = nums[3:]
            operations += 1
        
        return operations

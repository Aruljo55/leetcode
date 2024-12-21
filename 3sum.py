class Solution:
    def threeSum(self, nums):
        # Sort the array to apply the two-pointer approach
        nums.sort()
        res = []
        
        # Iterate through the array
        for i in range(len(nums) - 2):
            # Skip duplicate elements for the current position
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Initialize two pointers
            left, right = i + 1, len(nums) - 1
            
            # Use two pointers to find a valid triplet
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move left and right to the next different elements to avoid duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return res
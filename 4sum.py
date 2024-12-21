class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # Sort the array to use two-pointer technique
        res = []
        n = len(nums)
        
        # Iterate through the array
        for i in range(n - 3):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicate values for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicate values for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                        
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return res

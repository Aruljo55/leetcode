class Solution:
    def threeSumClosest(self, nums, target):
        # Sort the array to apply the two-pointer approach
        nums.sort()
        closest_sum = float('inf')  # Initialize with infinity to track the closest sum
        
        # Iterate through the array
        for i in range(len(nums) - 2):
            # Initialize two pointers
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                # Check if the current sum is closer to the target than the previous closest sum
                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total
                
                # Move pointers based on the comparison with the target
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    # If the total is exactly equal to the target, return it
                    return total
        
        return closest_sum

        
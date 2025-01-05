class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Pointer for the next unique position in the array
        i = 1  # Start from the second element
        
        # Traverse the array starting from the second element
        for j in range(1, len(nums)):
            # If the current number is the same as the previous one
            # Check if it has appeared twice already
            if nums[j] == nums[i - 1]:
                # Only allow the number if it has appeared less than twice
                if i > 1 and nums[i - 2] == nums[j]:
                    continue  # Skip this number if it appeared twice already
            # Place the number at the next available position in the result array
            nums[i] = nums[j]
            i += 1
        
        return i

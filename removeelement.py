class Solution:
    def removeElement(self, nums, val):
        # Pointer for the position where the next non-val element will go
        k = 0
        
        # Iterate through the entire array
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Place the element at the next valid position
                k += 1  # Move the pointer forward
        
        return k

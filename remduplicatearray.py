class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Initialize a pointer for the position of unique elements
        unique_pos = 0

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the last unique element
            if nums[i] != nums[unique_pos]:
                unique_pos += 1  # Move the unique position pointer
                nums[unique_pos] = nums[i]  # Update the array at unique position

        # Return the number of unique elements, which is unique_pos + 1
        return unique_pos + 1


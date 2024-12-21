class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to map numbers to their indices
        num_to_index = {}
        
        # Iterate through the list of numbers
        for index, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If found, return the indices of the complement and the current number
                return [num_to_index[complement], index]
            
            # Store the index of the current number in the dictionary
            num_to_index[num] = index

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)  # Output: [0, 1]

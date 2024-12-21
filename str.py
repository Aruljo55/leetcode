class Solution:
    def lengthOfLongestSubstring(self, s):
        # Dictionary to store the last index of each character in the string
        char_index_map = {}
        
        # Initialize the start of the sliding window and the maximum length of the substring
        start = 0
        max_length = 0
        
        # Iterate through the string using the index and character
        for i, char in enumerate(s):
            # If the character is already in the map and its index is within the current window
            if char in char_index_map and char_index_map[char] >= start:
                # Move the start of the window right after the last occurrence of the current character
                start = char_index_map[char] + 1
            
            # Update the character's latest index in the map
            char_index_map[char] = i
            
            # Calculate the length of the current substring and update max_length if it's larger
            max_length = max(max_length, i - start + 1)
        
        return max_length


        
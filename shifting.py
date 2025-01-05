class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        shift_delta = [0] * (n + 1)  # Array to track the shift deltas
        
        # Step 1: Accumulate shift deltas
        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            shift_delta[start] += shift_value
            if end + 1 < n:
                shift_delta[end + 1] -= shift_value
        
        # Step 2: Compute total shifts for each index
        current_shift = 0
        s = list(s)  # Convert the string to a list for easier mutation
        for i in range(n):
            current_shift += shift_delta[i]
            
            # Apply the shift to the character at index i
            char = s[i]
            shift = current_shift % 26  # Ensure the shift is within the range [0, 25]
            
            if shift != 0:
                # Shifting forward if shift > 0, or backward if shift < 0
                new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                s[i] = new_char
        
        return ''.join(s)

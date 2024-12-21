class Solution:
    def romanToInt(self, s):
        # Map of Roman numerals to their integer values
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate over the Roman numeral from left to right
        for char in s:
            # Get the integer value of the current Roman numeral
            curr_value = roman_to_int[char]
            
            # If the current value is greater than the previous value, it means we encountered a subtractive combination
            if curr_value > prev_value:
                # Subtract twice the previous value to correct the previously added value and account for the subtraction
                total += curr_value - 2 * prev_value
            else:
                # Add the current value to the total
                total += curr_value
                
            # Update the previous value to the current one for the next iteration
            prev_value = curr_value
        
        return total

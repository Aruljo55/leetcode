class Solution:
    def letterCombinations(self, digits):
        # Edge case: if the input is empty, return an empty list
        if not digits:
            return []
        
        # Mapping of digits to corresponding letters
        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        
        # List to store the result combinations
        result = []
        
        # Helper function for backtracking
        def backtrack(index, current_combination):
            # If the current combination has the same length as the digits, add it to the result
            if index == len(digits):
                result.append(current_combination)
                return
            
            # Get the possible letters for the current digit
            current_digit = digits[index]
            possible_letters = digit_to_letters[current_digit]
            
            # Iterate over the possible letters and recursively build combinations
            for letter in possible_letters:
                backtrack(index + 1, current_combination + letter)
        
        # Start the backtracking with index 0 and an empty current combination
        backtrack(0, "")
        
        return result

        
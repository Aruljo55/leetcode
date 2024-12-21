class Solution:
    def convert(self, s, numRows):
        # Edge case: if numRows is 1, the zigzag pattern is just the original string
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize an array of empty strings for each row
        rows = [''] * numRows
        
        # Variables to track the current row and direction (up or down)
        curr_row = 0
        going_down = False

        # Iterate over each character in the string
        for char in s:
            # Add the current character to the current row
            rows[curr_row] += char

            # If we are at the top or bottom row, change direction
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down

            # Move to the next row
            curr_row += 1 if going_down else -1

        # Concatenate all rows to get the final zigzag string
        return ''.join(rows)

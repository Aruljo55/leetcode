class Solution:
    def generate(self, numRows):
        # Initialize the result list with the first row
        pascal = [[1]]
        
        # Build each row from the second to numRows
        for i in range(1, numRows):
            # Start each row with 1
            row = [1]
            # Add the sum of the two elements above
            for j in range(1, i):
                row.append(pascal[i-1][j-1] + pascal[i-1][j])
            # End each row with 1
            row.append(1)
            # Append the row to Pascal's triangle
            pascal.append(row)
        
        return pascal

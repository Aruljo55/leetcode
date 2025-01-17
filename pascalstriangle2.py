class Solution:
    def getRow(self, rowIndex):
        # Start with the first row
        row = [1]
        
        # Build each row up to rowIndex
        for i in range(1, rowIndex + 1):
            # Update the row in reverse to calculate the current row
            row.append(1)
            for j in range(len(row) - 2, 0, -1):
                row[j] += row[j - 1]
        
        return row

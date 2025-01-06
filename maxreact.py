class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols  # Heights array for the histogram
        max_area = 0
        
        for row in matrix:
            for j in range(cols):
                # Update heights: Increment if '1', reset to 0 if '0'
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            
            # Calculate the largest rectangle for this histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)
        
        while stack:
            h = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, h * width)
        
        return max_area

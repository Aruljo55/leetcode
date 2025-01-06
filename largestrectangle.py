class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # Stack to store indices
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            # While stack is not empty and the current height is less than the height of the bar at the top of the stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Height of the bar
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)
        
        # Calculate area for remaining bars in the stack
        while stack:
            h = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, h * width)
        
        return max_area

class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the width between the two lines
            width = right - left
            # Calculate the height of the container, which is the shorter of the two lines
            min_height = min(height[left], height[right])
            # Calculate the current area
            current_area = width * min_height
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer from the shorter line to try and find a taller one
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

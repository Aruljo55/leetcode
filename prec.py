class Solution:
    def isRectangleCover(self, rectangles) -> bool:
        area = 0
        corner_points = set()
        
        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')
        
        for x1, y1, x2, y2 in rectangles:
            # Update bounding box
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            
            # Calculate area
            area += (x2 - x1) * (y2 - y1)
            
            # For each corner toggle in the set
            for point in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if point in corner_points:
                    corner_points.remove(point)
                else:
                    corner_points.add(point)
        
        # Check if total area matches the bounding rectangle
        expected_area = (max_x - min_x) * (max_y - min_y)
        if area != expected_area:
            return False
        
        # Check corners: must be exactly the four corners of bounding rectangle
        expected_corners = set([
            (min_x, min_y), 
            (min_x, max_y), 
            (max_x, min_y), 
            (max_x, max_y)
        ])
        return corner_points == expected_corners

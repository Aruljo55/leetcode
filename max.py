from collections import defaultdict

# Custom implementation of gcd (Greatest Common Divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def maxPoints(self, points):
        def max_points_on_line_from_point(i):
            slopes = defaultdict(int)
            same_point = 0
            vertical = 0
            max_count = 0
            
            for j in range(len(points)):
                if i == j:
                    continue
                
                # Handle case where both points are the same
                if points[i] == points[j]:
                    same_point += 1
                    continue
                
                # Handle vertical lines (undefined slope)
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0:
                    vertical += 1
                    continue
                
                # Calculate the slope using GCD to avoid precision issues
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                
                # Ensure the slope is always represented in the same direction
                if dx < 0:
                    dx, dy = -dx, -dy
                
                slopes[(dx, dy)] += 1
                max_count = max(max_count, slopes[(dx, dy)])
            
            # Max points on the same line considering duplicates and verticals
            return max(max_count + same_point + 1, vertical + same_point + 1)
        
        if len(points) <= 1:
            return len(points)
        
        result = 0
        for i in range(len(points)):
            result = max(result, max_points_on_line_from_point(i))
        
        return result

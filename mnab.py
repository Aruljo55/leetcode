class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # Sort balloons by their ending x-coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        last_end = points[0][1]

        for start, end in points[1:]:
            # If current balloon starts after the last arrow position
            if start > last_end:
                arrows += 1
                last_end = end

        return arrows

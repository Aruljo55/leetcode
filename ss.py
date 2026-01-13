class Solution:
    def findMinimumY(self, squares):
        total = 0
        min_y = float('inf')
        max_y = 0

        for _, y, l in squares:
            total += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        half = total / 2.0

        def area_below(y):
            area = 0.0
            for _, y0, l in squares:
                if y <= y0:
                    continue
                elif y >= y0 + l:
                    area += l * l
                else:
                    area += (y - y0) * l
            return area

        left, right = min_y, max_y
        for _ in range(60):
            mid = (left + right) / 2
            if area_below(mid) < half:
                left = mid
            else:
                right = mid

        return left

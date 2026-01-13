class Solution:
    def separateSquares(self, squares):
        total = 0.0
        min_y = 10**30
        max_y = 0

        for _, y, l in squares:
            total += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        half = total / 2.0

        def area_below(h):
            area = 0.0
            for _, y, l in squares:
                if h <= y:
                    continue
                area += min(h - y, l) * l
            return area

        left, right = min_y, max_y

        for _ in range(80):
            mid = (left + right) / 2.0
            if area_below(mid) < half:
                left = mid
            else:
                right = mid

        return (left + right) / 2.0

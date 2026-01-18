class Solution:
    def numberOfBoomerangs(self, points):
        result = 0

        for x1, y1 in points:
            dist_count = {}

            for x2, y2 in points:
                dx = x1 - x2
                dy = y1 - y2
                dist = dx * dx + dy * dy

                dist_count[dist] = dist_count.get(dist, 0) + 1

            for count in dist_count.values():
                result += count * (count - 1)

        return result

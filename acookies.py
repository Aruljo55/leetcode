class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        i = j = 0
        count = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return count

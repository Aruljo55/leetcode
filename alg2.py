class Solution:
    def countAlternatingGroups(self, colors, k):
        n = len(colors)
        extended_colors = colors + colors[:k-1]  # Extend to handle circular wrap-around
        count = 0
        
        # Check all k-length windows
        for i in range(n):
            valid = True
            for j in range(i, i + k - 1):
                if extended_colors[j] == extended_colors[j + 1]:  # Not alternating
                    valid = False
                    break
            if valid:
                count += 1
        
        return count

# Example usage
solution = Solution()
colors = [0, 1, 0, 1, 0]
k = 3
print(solution.countAlternatingGroups(colors, k))  # Output: 3

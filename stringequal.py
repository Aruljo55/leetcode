class Solution:
    def areAlmostEqual(self, s1, s2):
        if s1 == s2:
            return True
        
        diff = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]
        
        return len(diff) == 2 and diff[0] == diff[1][::-1]

# Example usage:
sol = Solution()
print(sol.areAlmostEqual("bank", "kanb"))  # Output: True
print(sol.areAlmostEqual("attack", "defend"))  # Output: False
print(sol.areAlmostEqual("kelb", "kelb"))  # Output: True

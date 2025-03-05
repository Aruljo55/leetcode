class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                right = mid  # Move left to find the first bad version
            else:
                left = mid + 1  # Move right to skip the good version
        
        return left

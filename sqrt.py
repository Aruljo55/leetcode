class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x  # 0 or 1 are their own square roots
        
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid  # Perfect square
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return high  # high is the largest integer such that high^2 <= x

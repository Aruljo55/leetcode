class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        while n:
            if n % 2:  # If n is odd
                result *= x
            x *= x  # Square the base
            n //= 2  # Divide n by 2
        
        return result

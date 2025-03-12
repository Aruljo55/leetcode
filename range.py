class Solution:
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def closestPrimes(self, left, right):
        primes = []
        # Collect all prime numbers in the range
        for i in range(left, right + 1):
            if self.is_prime(i):
                primes.append(i)
        
        if len(primes) < 2:
            return [-1, -1]
        
        min_gap = float('inf')
        result = [-1, -1]
        
        # Find the pair with the smallest gap
        for i in range(1, len(primes)):
            if primes[i] - primes[i-1] < min_gap:
                min_gap = primes[i] - primes[i-1]
                result = [primes[i-1], primes[i]]
        
        return result

# Example Test Cases
solution = Solution()
print(solution.closestPrimes(10, 19))  # Output: [11, 13]
print(solution.closestPrimes(4, 6))    # Output: [-1, -1]
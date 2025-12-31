class Solution:
    def nthSuperUglyNumber(self, n, primes):
        size = len(primes)
        ugly = [1] * n  # This will hold our super ugly numbers
        idx = [0] * size  # Pointers for each prime
        values = list(primes)  # Current values from primes * ugly[idx[i]]

        for i in range(1, n):
            # Next ugly number is the minimum of all current prime * ugly[idx]
            next_ugly = min(values)
            ugly[i] = next_ugly

            # Update the pointer(s) that matched the next ugly number
            for j in range(size):
                if values[j] == next_ugly:
                    idx[j] += 1
                    values[j] = primes[j] * ugly[idx[j]]

        return ugly[-1]

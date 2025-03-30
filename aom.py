MOD = 10**9 + 7

class Solution:
    def count_distinct_prime_factors(self, limit):
        # Sieve of Eratosthenes to compute the number of distinct prime factors for each number
        prime_factors = [0] * (limit + 1)
        for i in range(2, limit + 1):
            if prime_factors[i] == 0:  # i is a prime number
                for j in range(i, limit + 1, i):
                    prime_factors[j] += 1
        return prime_factors

    def maximizeScore(self, nums, k):
        n = len(nums)
        max_val = 10**5
        prime_factors = self.count_distinct_prime_factors(max_val)
        
        # Create a list of (prime_score, value, index)
        score_info = [(prime_factors[num], num, idx) for idx, num in enumerate(nums)]
        
        # Sort by prime score descending, and then by index ascending
        score_info.sort(key=lambda x: (-x[0], x[2]))
        
        # Calculate the result by taking the first k elements
        result = 1
        for i in range(min(k, n)):
            result = (result * score_info[i][1]) % MOD
        
        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums1 = [8, 3, 9, 3, 8]
    k1 = 2
    print(solution.maximizeScore(nums1, k1))  # Output: 81

    nums2 = [19, 12, 14, 6, 10, 18]
    k2 = 3
    print(solution.maximizeScore(nums2, k2))  # Output: 4788

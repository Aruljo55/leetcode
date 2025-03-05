class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        odd_count = even_count = result = 0
        for num in arr:
            if num % 2 == 1:
                odd_count, even_count = even_count + 1, odd_count
            else:
                odd_count, even_count = odd_count, even_count + 1
            result = (result + odd_count) % MOD
        return result

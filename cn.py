class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def mod_pow(base, exp):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return result

        even_count = (n + 1) // 2
        odd_count = n // 2

        return (mod_pow(5, even_count) * mod_pow(4, odd_count)) % MOD

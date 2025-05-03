class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337
        
        def powmod(x, n):
            x %= MOD
            result = 1
            for _ in range(n):
                result = (result * x) % MOD
            return result

        def helper(b):
            if not b:
                return 1
            last_digit = b.pop()
            part1 = powmod(self.superPow(a, b), 10)
            part2 = powmod(a, last_digit)
            return (part1 * part2) % MOD

        return helper(b)

from itertools import permutations
from collections import Counter

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Set to store digit frequency patterns of valid k-palindromic numbers
        valid_digit_sets = set()

        # Generate all palindromic numbers of length n
        def generate_palindromes():
            half = (n + 1) // 2
            start = 10**(half - 1)
            end = 10**half
            for i in range(start, end):
                left = str(i)
                if n % 2 == 0:
                    full = left + left[::-1]
                else:
                    full = left + left[:-1][::-1]
                if full[0] != '0':
                    num = int(full)
                    if num % k == 0:
                        digit_count = tuple(sorted(Counter(full).items()))
                        valid_digit_sets.add(digit_count)

        generate_palindromes()

        # Now count all n-digit numbers whose digits match a valid digit set
        start = 10**(n - 1)
        end = 10**n
        ans = 0
        for num in range(start, end):
            digit_count = tuple(sorted(Counter(str(num)).items()))
            if digit_count in valid_digit_sets:
                ans += 1

        return ans

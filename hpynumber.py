class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)
        return s

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1

# Example usage
solution = Solution()
print(solution.removeOccurrences("daabcbaabcbc", "abc"))  # Output: "dab"
print(solution.removeOccurrences("axxxxyyyyb", "xy"))  # Output: "ab"
print(solution.rangeBitwiseAnd(5, 7))  # Output: 4
print(solution.rangeBitwiseAnd(0, 0))  # Output: 0
print(solution.rangeBitwiseAnd(1, 2147483647))  # Output: 0
print(solution.isHappy(19))  # Output: True
print(solution.isHappy(2))  # Output: False
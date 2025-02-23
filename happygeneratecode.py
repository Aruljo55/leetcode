from itertools import product

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def is_happy(s):
            return all(s[i] != s[i + 1] for i in range(len(s) - 1))
        
        happy_strings = sorted("".join(p) for p in product("abc", repeat=n) if is_happy(p))
        return happy_strings[k - 1] if k <= len(happy_strings) else ""

# Example usage:
solution = Solution()
print(solution.getHappyString(3, 9))
from itertools import product

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def is_happy(s):
            return all(s[i] != s[i + 1] for i in range(len(s) - 1))
        
        happy_strings = sorted("".join(p) for p in product("abc", repeat=n) if is_happy(p))
        return happy_strings[k - 1] if k <= len(happy_strings) else ""

# Example usage:
solution = Solution()
print(solution.getHappyString(3, 9))

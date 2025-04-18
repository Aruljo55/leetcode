import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.isqrt(n))  # or use math.sqrt(n) and take int()

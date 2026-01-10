class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = has_upper = has_digit = 0
        for c in password:
            if c.islower():
                has_lower = 1
            elif c.isupper():
                has_upper = 1
            elif c.isdigit():
                has_digit = 1

        missing = 3 - (has_lower + has_upper + has_digit)

        i = 0
        replace = 0
        one = two = 0

        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                replace += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            i = j

        if n < 6:
            return max(missing, 6 - n)

        if n <= 20:
            return max(missing, replace)

        delete = n - 20

        use = min(delete, one)
        replace -= use
        delete -= use

        use = min(delete // 2, two)
        replace -= use
        delete -= use * 2

        use = delete // 3
        replace -= use

        return (n - 20) + max(missing, replace)

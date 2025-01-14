class Solution:
    def canBeValid(self, s, locked):
        # If the length of the string is odd, it cannot be valid
        if len(s) % 2 != 0:
            return False

        n = len(s)
        open_flex = close_flex = 0

        # Left to Right pass
        for i in range(n):
            if locked[i] == '0' or s[i] == '(':
                open_flex += 1  # Either '(' or a flexible position
            else:
                open_flex -= 1  # A fixed ')'
            
            # If we have more ')' than '(' + flexibility at any point, it's invalid
            if open_flex < 0:
                return False

        # Right to Left pass
        for i in range(n - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                close_flex += 1  # Either ')' or a flexible position
            else:
                close_flex -= 1  # A fixed '('
            
            # If we have more '(' than ')' + flexibility at any point, it's invalid
            if close_flex < 0:
                return False

        return True

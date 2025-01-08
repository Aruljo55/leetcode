class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False

        # Memoization dictionary
        memo = {}

        def dfs(s1, s2):
            # Check memoization
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            # Base case
            if s1 == s2:
                memo[(s1, s2)] = True
                return True

            # Quick check
            if sorted(s1) != sorted(s2):  # If character frequencies don't match
                memo[(s1, s2)] = False
                return False

            n = len(s1)
            for i in range(1, n):  # Split at every possible position
                # Without swap: s1[:i] matches s2[:i] AND s1[i:] matches s2[i:]
                if dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                # With swap: s1[:i] matches s2[-i:] AND s1[i:] matches s2[:-i]
                if dfs(s1[:i], s2[-i:]) and dfs(s1[i:], s2[:-i]):
                    memo[(s1, s2)] = True
                    return True

            # If no valid split found
            memo[(s1, s2)] = False
            return False

        return dfs(s1, s2)

class Solution:
    def findKthNumber(self, n, k):
        def count_prefix(prefix, n):
            """Count how many numbers starting with `prefix` are <= n."""
            count = 0
            curr, next_prefix = prefix, prefix + 1
            while curr <= n:
                count += min(n + 1, next_prefix) - curr
                curr *= 10
                next_prefix *= 10
            return count

        curr = 1
        k -= 1  # start counting from 1
        while k > 0:
            steps = count_prefix(curr, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        return curr

# Example usage:
sol = Solution()
print(sol.findKthNumber(13, 2))  # Output: 10
print(sol.findKthNumber(1, 1))   # Output: 1

from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)   # Count of characters in p
        s_count = Counter(s[:np])  # Initial window in s

        result = []
        if s_count == p_count:
            result.append(0)

        # Slide the window
        for i in range(1, ns - np + 1):
            left_char = s[i-1]
            right_char = s[i + np - 1]

            # Remove the left_char from the window
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]

            # Add the new right_char
            s_count[right_char] += 1

            if s_count == p_count:
                result.append(i)

        return result

# Example usage
s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))  # Output: [0, 6]

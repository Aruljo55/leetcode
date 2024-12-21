class Solution:
    def countAndSay(self, n):
        def next_sequence(s):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    i += 1
                    count += 1
                result.append(str(count) + s[i])
                i += 1
            return ''.join(result)

        sequence = "1"
        for _ in range(n - 1):
            sequence = next_sequence(sequence)
        return sequence

if __name__ == "__main__":
    solution = Solution()
    n = 4
    print(solution.countAndSay(n))

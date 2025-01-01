class Solution:
    def maxScore(self, s):
        # Initialize the maximum score
        max_score = 0

        # Precompute the total number of ones in the string
        total_ones = s.count('1')

        # Initialize counters for zeros on the left and ones on the right
        left_zeros = 0
        right_ones = total_ones

        # Iterate through the string and compute scores
        # Stop at len(s) - 1 to ensure non-empty substrings
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                right_ones -= 1

            # Calculate the current score
            score = left_zeros + right_ones

            # Update the maximum score
            max_score = max(max_score, score)

        return max_score

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxScore("011101"))  # Output: 5
    print(solution.maxScore("00111"))   # Output: 5
    print(solution.maxScore("1111"))    # Output: 3

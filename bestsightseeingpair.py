class Solution:
    def maxScoreSightseeingPair(self, values):
        max_score = 0
        max_i = values[0]  # values[0] + 0 since the index is 0

        for j in range(1, len(values)):
            # Calculate the score for the pair (i, j) using max_i
            max_score = max(max_score, max_i + values[j] - j)
            # Update max_i for the next iteration
            max_i = max(max_i, values[j] + j)

        return max_score

# Example usage
# If running in a competitive programming platform, you don't need the lines below.
# They are for standalone testing.
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxScoreSightseeingPair([8, 1, 5, 2, 6]))  # Output: 11
    print(solution.maxScoreSightseeingPair([1, 2]))           # Output: 2

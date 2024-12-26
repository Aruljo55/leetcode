from math import factorial

class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        k -= 1  # Convert k to zero-based index
        result = []

        for i in range(n):
            fact = factorial(n - 1 - i)
            index = k // fact
            result.append(str(numbers.pop(index)))
            k %= fact

        return ''.join(result)

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.getPermutation(3, 3))  # Output: "213"
    print(solution.getPermutation(4, 9))  # Output: "2314"
    print(solution.getPermutation(3, 1))  # Output: "123"

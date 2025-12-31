class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        result = "1"
        
        # Generate the sequence iteratively from 2 to n
        for _ in range(1, n):
            next_result = ""
            count = 1
            # Iterate through the string and perform RLE
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    next_result += str(count) + result[i - 1]
                    count = 1
            # Append the last sequence
            next_result += str(count) + result[-1]
            
            # Update the result for the next iteration
            result = next_result
        
        return result

# Driver code for testing
if __name__ == "__main__":
    solution = Solution()
    print(solution.countAndSay(4))  # Output: "1211"
    print(solution.countAndSay(1))  # Output: "1"

class Solution:
    def minAddToMakeValid(self, s):
        open_needed = 0
        close_needed = 0
        
        for char in s:
            if char == '(':
                close_needed += 1
            elif char == ')':
                if close_needed > 0:
                    close_needed -= 1
                else:
                    open_needed += 1
        
        return open_needed + close_needed

# Example Test Cases
solution = Solution()
print(solution.minAddToMakeValid("())"))  # Output: 1
print(solution.minAddToMakeValid("((("))  # Output: 3

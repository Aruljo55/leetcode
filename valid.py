class Solution:
    def isValid(self, s):
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map:
                # Check if the top of the stack matches the corresponding opening bracket
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)
        
        # If the stack is empty, all opening brackets were matched
        return not stack

# Example usage
s = "()[]{}"  # Change this to test different inputs
solution = Solution()
print(solution.isValid(s))  # Output: True
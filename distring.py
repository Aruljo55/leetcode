class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = ""
        num = 1
        
        for char in pattern:
            stack.append(str(num))
            num += 1
            if char == 'I':
                while stack:
                    result += stack.pop()
        
        stack.append(str(num))
        while stack:
            result += stack.pop()
        
        return result

# Example usage
sol = Solution()
print(sol.smallestNumber("IIIDIDDD"))  # Output: "123549876"
print(sol.smallestNumber("DDD"))       # Output: "4321"

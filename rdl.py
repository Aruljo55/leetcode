class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            if char in seen:
                continue
            # Ensure lexicographically smallest result
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)
